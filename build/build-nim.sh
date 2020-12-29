#!/bin/sh

set -uex

SCRIPT_DIR="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
cd "${SCRIPT_DIR}/src"

nim_dir=$1

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
