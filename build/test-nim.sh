#!/bin/sh

set -uex

SCRIPT_DIR="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

SRC_DIR=${1:-"${SCRIPT_DIR}/src"}

cd "$SRC_DIR"

major=$(bin/nim -v | head -n1 | sed 's/.* Version \([0-9]\{1,\}\)\.\([0-9]\{1,\}\)\.\([0-9]\{1,\}\) .*/\1/')
minor=$(bin/nim -v | head -n1 | sed 's/.* Version \([0-9]\{1,\}\)\.\([0-9]\{1,\}\)\.\([0-9]\{1,\}\) .*/\2/')
patch=$(bin/nim -v | head -n1 | sed 's/.* Version \([0-9]\{1,\}\)\.\([0-9]\{1,\}\)\.\([0-9]\{1,\}\) .*/\3/')

test () {
  target=$1
  extra_args=""
  skip_file="../nim-${major}.${minor}.${patch}-${target}-skip-tests.txt"
  if [ -f "$skip_file" ]
  then
    extra_args="--skipFrom:${skip_file}"
  else
    skip_file="../nim-${major}.${minor}-${target}-skip-tests.txt"
    if [ -f "$skip_file" ]
    then
      extra_args="--skipFrom:${skip_file}"
    fi
  fi
  testament/testament --nim:bin/nim --targets:$target $extra_args all
}

if [ "$(which apk)" != "" ]
then
  apk add --update --no-cache sfml prcre gc sqlite-dev sqlite
elif [ "$(which apt)" != "" ]
then
  apt-get update -q -y
  apt-get -qq install -y libcsfml-dev libpcre3 libgc-dev libgc1c2 sqlite3
elif [ "$(which pacman)" != "" ]
then
  pacman -Syu --noconfirm sfml pcre gc sqlite
  pacman -Sc --noconfirm || true
elif [ "$(which brew)" != "" ]
then
  brew install sfml sqlite
fi

bin/nim cc --opt:speed testament/testament

test c
test c++
test js
