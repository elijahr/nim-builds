#!/bin/sh

set -uex

NIM_DIR=$1

cd "${NIM_DIR}"

sh build.sh
bin/nim c koch
./koch boot -d:release
./koch tools -d:release
