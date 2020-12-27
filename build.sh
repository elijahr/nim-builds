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
elif [ "$(which apt)" != "" ]
then
  apt-get update -q -y
  apt-get -qq install -y wget xz-utils $extra_packages
elif [ "$(which pacman)" != "" ]
then
  pacman -Syu --noconfirm wget xz $extra_packages
  pacman -Sc --noconfirm || true
elif [ "$(which brew)" != "" ]
then
  brew install wget xz $extra_packages
fi

cd /code

dir="nim-${NIM_VERSION}-$(gcc -dumpmachine)"

if [ ! -d "$dir" ]
then
  wget "https://nim-lang.org/download/nim-${NIM_VERSION}.tar.xz"
  tar xJf "nim-${NIM_VERSION}.tar.xz"
  rm "nim-${NIM_VERSION}.tar.xz"
  mv "nim-${NIM_VERSION}" "$dir"
fi

cd "$dir"
if [ "$DEBUG" = "yes" ]
then
  sh build.sh --extraBuildArgs "-g"
  # strip ptrace since we're debugging in QEMU and ptrace isn't supported
  sed -i 's|ptrace|isnanl|' bin/nim
  valgrind -k bin/nim c koch
else
  sh build.sh
  bin/nim c koch
fi
./koch boot -d:release
./koch tools
cd -

tarball="${dir}.tar.xz"
tar -cJf "$tarball" "$dir"

echo "::set-output name=asset_name::${tarball}"
echo "::set-output name=asset_path::/code/${tarball}"
