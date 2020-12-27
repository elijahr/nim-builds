#!/bin/sh

set -uex

NIM_VERSION=$1
DEBUG=${2:-no}

if [ "$DEBUG" = "yes" ]
then
  extra_packages="valgrind"
else
  extra_packages=""
fi

if [ "$(which apk)" != "" ]
then
  apk add --update --no-cache wget xz $extra_packages
  apk add --update --no-cache pixz --repository=http://dl-cdn.alpinelinux.org/alpine/edge/testing
  tarball="nim-${NIM_VERSION}-$(gcc -dumpmachine | sed 's/alpine-//').tar.xz"
elif [ "$(which apt)" != "" ]
then
  apt-get update -q -y
  apt-get -qq install -y wget xz-utils pixz $extra_packages
elif [ "$(which pacman)" != "" ]
then
  pacman -Syu --noconfirm wget xz pixz $extra_packages
  pacman -Sc --noconfirm || true
elif [ "$(which brew)" != "" ]
then
  brew install wget xz pixz $extra_packages
fi

cd /code

dir="nim-${NIM_VERSION}-$(gcc -dumpmachine)"

if [ ! -d "$dir" ]
then
  wget "https://nim-lang.org/download/nim-${NIM_VERSION}.tar.xz" -O- | pixz -d | tar x
  mv "nim-${NIM_VERSION}" "$dir"
fi

cd "$dir"
if [ "$DEBUG" = "yes" ]
then
  sh build.sh --extraBuildArgs "-g"
  valgrind -k bin/nim c koch
else
  sh build.sh
  bin/nim c koch
fi
./koch boot -d:release
./koch tools
cd -

tarball="${dir}.tar.xz"
tar -c "$dir" | pixz > "$tarball"

echo "::set-output name=asset_name::${tarball}"
echo "::set-output name=asset_path::${PWD}/${tarball}"
