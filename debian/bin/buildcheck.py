#!/usr/bin/python3

import itertools
import os
import pathlib
import sys

from debian_linux.config_v2 import Config
from debian_linux.debian import Changelog, VersionLinux
from debian_linux.kconfig import KconfigFile


class CheckKernelSize(object):
    def __init__(self, config, dir, arch, featureset, flavour):
        self.changelog = Changelog(version=VersionLinux)[0]
        self.config = config
        self.dir = dir

    def __call__(self, out):
        limit = self.config.build.kernel_file_max_size
        if limit is None:
            return 0

        image = self.dir / self.config.build.kernel_file
        size = image.stat().st_size
        usage = (float(size) / limit) * 100.0

        out.write(f'Image size {size}/{limit}, using {usage:.2f}%.  ')

        if size > limit:
            out.write('Too large.  Refusing to continue.\n')
            return 1

        # 1% overhead is desirable in order to cope with growth
        # through the lifetime of a stable release. Warn if this is
        # not the case.
        if usage >= 99.0:
            out.write(f'Under 1% space in {self.changelog.distribution}.  ')
        else:
            out.write('Image fits.  ')
        out.write('Continuing.\n')
        return 0


class CheckSecureBootConfig:
    def __init__(self, config, dir, *_):
        self.config = config
        self.dir = dir

    def __call__(self, out):
        fail = 0

        if self.config.build.enable_signed \
           and not os.getenv('DEBIAN_KERNEL_DISABLE_SIGNED'):
            kconfig = KconfigFile()
            with (self.dir / '.config').open() as fh:
                kconfig.read(fh)

            for name, value in [('EFI_STUB', True),
                                ('LOCK_DOWN_IN_EFI_SECURE_BOOT', True),
                                ('SYSTEM_TRUSTED_KEYS', '""')]:
                if name not in kconfig:
                    out.write(f'Secure Boot: CONFIG_{name} is not defined\n')
                    fail = 1
                elif kconfig[name].value != value:
                    out.write(f'Secure Boot: CONFIG_{name} has wrong value:'
                              f' {kconfig[name].value}\n')
                    fail = 1

            if kconfig.get('MODULE_SIG_KEY').value == '"certs/signing_key.pem"':
                out.write('Secure Boot: CONFIG_MODULE_SIG_KEY has default value\n')
                fail = 1

        return fail


class Main(object):

    checks = {
        'setup': [CheckSecureBootConfig],
        'build': [CheckKernelSize],
    }

    def __init__(self, dir, arch, featureset, flavour, phase):
        self.args = pathlib.Path(dir), arch, featureset, flavour
        self.phase = phase

        config_dirs = [
            pathlib.Path('debian/config'),
            pathlib.Path('debian/config.local'),
        ]
        top_config = Config.read_orig(config_dirs).merged
        arch_config = next(
            ac
            for ac in itertools.chain.from_iterable(
                kac.debianarchs for kac in top_config.kernelarchs)
            if ac.name == arch
        )
        fs_config = next(fsc for fsc in arch_config.featuresets
                         if fsc.name == featureset)
        self.config = next(fc for fc in fs_config.flavours
                           if fc.name == flavour)

    def __call__(self):
        fail = 0

        for c in self.checks[self.phase]:
            fail |= c(self.config, *self.args)(sys.stdout)

        return fail


if __name__ == '__main__':
    sys.exit(Main(*sys.argv[1:])())
