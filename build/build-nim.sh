#!/bin/sh

set -uex

SCRIPT_DIR="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
cd "${SCRIPT_DIR}/src"

nim_dir=$1

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

sh build.sh
bin/nim c koch
./koch boot -d:release
./koch tools -d:release

rm -Rf "../${nim_dir}"
mkdir "../${nim_dir}"
./install.sh "../${nim_dir}"
for fn in nimble nimsuggest nimgrep
do
  cp "./bin/${fn}" "../${nim_dir}/nim/bin/"
done

echo "::set-output name=asset_name::${nim_dir}-$(gcc -dumpmachine).tar.xz"
