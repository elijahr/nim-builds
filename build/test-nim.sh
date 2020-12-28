#!/bin/sh

set -uex

SCRIPT_DIR="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

SRC_DIR=${1:-"${SCRIPT_DIR}/src"}

cd "$SRC_DIR"

test () {
  target=$1
  testament/testament --nim:bin/nim --targets:$target all
}

main () {
  if [ "$(which apk)" != "" ]
  then
    apk add --update --no-cache sfml pcre gc sqlite-dev sqlite
  elif [ "$(which apt)" != "" ]
  then
    apt-get update -q -y
    apt-get -qq install -y libcsfml-dev libpcre3 libgc-dev libgc1c2 sqlite3 libsqlite3-0 libsqlite3-dev
  elif [ "$(which pacman)" != "" ]
  then
    pacman -Syu --noconfirm sfml pcre gc sqlite
    pacman -Sc --noconfirm || true
  elif [ "$(which brew)" != "" ]
  then
    brew install sfml sqlite libgc
  fi

  bin/nim cc --opt:speed testament/testament

  test c
  test c++
  test js
}

main
