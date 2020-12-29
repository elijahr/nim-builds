#!/bin/sh

set -uex

NIM_DIR=$1

cd "${nim_dir}"

sh build.sh
bin/nim c koch
./koch boot -d:release
./koch tools -d:release
