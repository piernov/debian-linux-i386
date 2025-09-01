#!/bin/bash
set -euE

OUT=$(dirname $(realpath $0))
CHANGELOG="${OUT}/../../../../changelog"
VERSION=$(dpkg-parsechangelog -l "$CHANGELOG" -SVersion | sed -e 's/-[^-]*$//')

RANGE="v${VERSION}..v6.16"

git -c core.abbrev=12 --no-pager \
 log --format='format:### %h ("%s")%n```%ngit cherry-pick -xs %H%n```' \
 --no-merges --topo-order --reverse \
 "$RANGE" \
 -- drivers/infiniband/hw/mana/ drivers/net/ethernet/microsoft/ include/net/mana/
