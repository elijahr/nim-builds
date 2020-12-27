#!/bin/sh

set -uex

SCRIPT_DIR="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

SRC_DIR=${1:-"${SCRIPT_DIR}/src"}

cd "$SRC_DIR"

targets=("c" "c++" "js")

major=$(bin/nim -v | head -n1 | sed 's/.* Version \([0-9]\{1,\}\)\.\([0-9]\{1,\}\)\.\([0-9]\{1,\}\) .*/\1/')
minor=$(bin/nim -v | head -n1 | sed 's/.* Version \([0-9]\{1,\}\)\.\([0-9]\{1,\}\)\.\([0-9]\{1,\}\) .*/\2/')
patch=$(bin/nim -v | head -n1 | sed 's/.* Version \([0-9]\{1,\}\)\.\([0-9]\{1,\}\)\.\([0-9]\{1,\}\) .*/\3/')

bin/nim cc --opt:speed testament/testament

for target in ${targets[@]}
do
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
done
