#!/bin/sh

set -uex

NIM_DIR=$1

if [ "$(which apk)" != "" ]
then
  apk add --update --no-cache wget xz sfml
elif [ "$(which apt)" != "" ]
then
  apt-get update -q -y
  apt-get -qq install -y wget xz-utils libcsfml-dev
elif [ "$(which pacman)" != "" ]
then
  pacman -Syu --noconfirm wget xz sfml
  pacman -Sc --noconfirm || true
elif [ "$(which brew)" != "" ]
then
  brew install wget xz
fi

cd src
sh build.sh
bin/nim c koch
./koch boot -d:release
./koch docs
./koch tools -d:release
./koch test
rm -Rf "../${NIM_DIR}"
mkdir "../${NIM_DIR}"
./install.sh "../${NIM_DIR}"
for fn in nimble nimsuggest nimgrep
do
  cp "./bin/${fn}" "../${NIM_DIR}/nim/bin/"
done

echo "::set-output name=asset_name::${NIM_DIR}-$(gcc -dumpmachine).tar.xz"
