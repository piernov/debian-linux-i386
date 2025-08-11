#!/bin/bash
set -euE

OUT=$(dirname $(realpath $0))
CHANGELOG="${OUT}/../../../../changelog"
VERSION=$(dpkg-parsechangelog -l "$CHANGELOG" -SVersion | sed -e 's/-[^-]*$//')
TITLE=$(head -n 1 "${OUT}/README.md")

RANGE="v${VERSION}.."

git -C "$OUT" rm -q --ignore-unmatch '*.patch'
git format-patch -q -o "$OUT" "$RANGE"
git -C "$OUT" add '*.patch'
echo "$TITLE"
echo "# Taken from https://salsa.debian.org/waldi/linux-stable/ branch $(git rev-parse --abbrev-ref HEAD)"
find $(realpath "${OUT}/../../..") -path "${OUT}/*.patch" -printf '%P\n' | sort
