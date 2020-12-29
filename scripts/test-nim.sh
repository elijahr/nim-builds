#!/bin/sh

set -uex

SCRIPT_DIR="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

NIM_DIR=$1

cd "$NIM_DIR"

test () {
  target=$1
  category=$2
  PATH="${NIM_DIR}/bin:$PATH" \
    testament/testament \
    --nim:"${NIM_DIR}/bin/nim" \
    --targets:"$target" pcat "$category"
}

main () {
  "${NIM_DIR}/bin/nim" cc --opt:speed testament/testament

  # Run a small handful of tests
  test c compiler
  test c nimble
  test c++ compiler
}

main
