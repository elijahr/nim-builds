#!/bin/bash

set -uexo pipefail

SCRIPT_DIR="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
cd "${SCRIPT_DIR}/src"

targets=("C" "C++" "JS")

major=$(bin/nim -v | head -n1 | 's/.* Version \([0-9]\{1,\}\)\.\([0-9]\{1,\}\)\.\([0-9]\{1,\}\) .*/\1/')
minor=$(bin/nim -v | head -n1 | 's/.* Version \([0-9]\{1,\}\)\.\([0-9]\{1,\}\)\.\([0-9]\{1,\}\) .*/\2/')
patch=$(bin/nim -v | head -n1 | 's/.* Version \([0-9]\{1,\}\)\.\([0-9]\{1,\}\)\.\([0-9]\{1,\}\) .*/\3/')


bin/nim cc --opt:speed testament/testament

for in ${targets[@]}
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
  testament/testament --nim:bin/nim --targets:$target $extra_args
done
