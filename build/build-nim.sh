#!/bin/sh

set -uex

NIM_DIR=$1

if [ "$(which apk)" != "" ]
then
  apk add --update --no-cache wget xz
elif [ "$(which apt)" != "" ]
then
  apt-get update -q -y
  apt-get -qq install -y wget xz-utils
elif [ "$(which pacman)" != "" ]
then
  pacman -Syu --noconfirm wget xz
  pacman -Sc --noconfirm || true
elif [ "$(which brew)" != "" ]
then
  brew install wget xz
fi

cd "$NIM_DIR"
sh build.sh
bin/nim c koch
./koch boot -d:release
./koch tools

echo "::set-output name=asset_name::nim-${NIM_VERSION}-$(gcc -dumpmachine).tar.xz"
