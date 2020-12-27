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

dir="nim-${NIM_VERSION}-$(gcc -dumpmachine)"
tarball="${dir}.tar.xz"

if [ ! -d "$dir" ]
then
  if [ ! -f "nim-${NIM_VERSION}.tar.xz" ]
  then
    wget "https://nim-lang.org/download/nim-${NIM_VERSION}.tar.xz"
  fi
  tar -xJf "nim-${NIM_VERSION}.tar.xz"
  mv "nim-${NIM_VERSION}" "$dir"
fi

cd "$dir"
sh build.sh --extraBuildArgs "-ggdb"
bin/nim c koch
./koch boot -d:release
./koch tools
cd -

tar -cJf "$tarball" "$dir"

echo "::set-output name=asset_name::${tarball}"
echo "::set-output name=asset_path::${PWD}/${tarball}"
