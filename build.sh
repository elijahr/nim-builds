#!/bin/sh

set -uex

NIM_VERSION=$1


if [ "$(which apk)" != "" ]
then
  apk add --update --no-cache wget xz
  tarball="nim-${NIM_VERSION}-$(gcc -dumpmachine | sed 's/alpine-//').tar.xz"
elif [ "$(which apt)" != "" ]
then
  apt-get update -q -y
  apt-get -qq install -y wget xz-utils
elif [ "$(which brew)" != "" ]
then
  brew install wget xz
fi

cd /code

if [ ! -d "nim-${NIM_VERSION}" ]
then
  if [ ! -f "nim-${NIM_VERSION}.tar.xz" ]
  then
    wget "https://nim-lang.org/download/nim-${NIM_VERSION}.tar.xz"
  else
    tar -xJf nim-${NIM_VERSION}.tar.xz
  fi
fi

cd "nim-${NIM_VERSION}"
sh build.sh
bin/nim c koch
./koch boot -d:release
./koch tools
cd -

tarball="nim-${NIM_VERSION}-$(gcc -dumpmachine).tar.xz"
tar -cJf "$tarball" "nim-${NIM_VERSION}"

echo "::set-output name=asset_name::${tarball}"
echo "::set-output name=asset_path::${PWD}/${tarball}"
