#!/bin/sh

set -uex

SCRIPT_DIR="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

NIM_DIR="$( cd "$(dirname "$1")" >/dev/null 2>&1 ; pwd -P )/$(basename $1)"

cd "$NIM_DIR"

if [ -f "testament/testament.nim" ]
then
  tester=testament/testament
else
  # 0.X.X
  tester=testament/tester
fi

install_deps () {
  (apk add --update --no-cache build-base) || \
  (apt-get update -q -y && apt-get -qq install -y build-essential) || \
  (pacman -Syu --noconfirm base-devel && pacman -Sc --noconfirm) || \
  (dnf install -y make automake gcc gcc-c++ kernel-devel) || \
  true
}

test_nim () {
  target=$1
  category=$2
  PATH="${NIM_DIR}/bin:$PATH" \
    "$tester" \
    --nim:"${NIM_DIR}/bin/nim" \
    --targets:"$target" pcat "$category"
}

main () {
  install_deps
  "${NIM_DIR}/bin/nim" cc --opt:speed "$tester"

  # Run a small handful of tests
  test_nim c compiler
  test_nim c++ compiler
  test_nim c compilerapi
  test_nim c compilerfeatures
  test_nim c nimble
  test_nim c threads
}

main
