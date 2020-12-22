#!/bin/sh

set -uex

NIM_VERSION=$1

tarball="nim-${NIM_VERSION}-$(gcc -dumpmachine).tar.xz"

if [ "$(which apk)" != "" ]
then
  apk add --update --no-cache git xz
  tarball="nim-${NIM_VERSION}-$(gcc -dumpmachine | sed 's/alpine-//').tar.xz"
elif [ "$(which apt)" != "" ]
then
  apt-get update -q -y
  apt-get -qq install -y git xz-utils
fi

git clone -q --depth 1 --single-branch --branch "v${NIM_VERSION}" https://github.com/nim-lang/Nim.git
sh build_all.sh
export PATH=/Nim/bin:$PATH
./koch csource -d:danger
./koch xz

mv ./build/nim-*.tar.xz "/code/${tarball}"

echo "::set-output name=tarball::${tarball}"
