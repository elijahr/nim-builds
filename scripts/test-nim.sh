#!/bin/sh

set -uex

SCRIPT_DIR="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

NIM_DIR=$1

cd "$NIM_DIR"

install_deps () {
  if [ "$(which apk)" != "" ]
  then
    # Alpine
    apk add --update --no-cache build-base
  elif [ "$(which apt)" != "" ]
  then
    # Debian, Ubuntu
    apt-get update -q -y
    apt-get -qq install -y build-essential
  elif [ "$(which pacman)" != "" ]
  then
    # Arch, Manjaro
    pacman -Syu --noconfirm base-devel
    pacman -Sc --noconfirm || true
  fi
}

test () {
  target=$1
  category=$2
  PATH="${NIM_DIR}/bin:$PATH" \
    testament/testament \
    --nim:"${NIM_DIR}/bin/nim" \
    --targets:"$target" pcat "$category"
}

main () {
  install_deps
  "${NIM_DIR}/bin/nim" cc --opt:speed testament/testament

  # Run a small handful of tests
  test c compiler
  test c nimble
  test c++ compiler
}

main
