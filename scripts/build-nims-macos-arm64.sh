#!/usr/bin/env bash

set -uex

dir="$(realpath $(dirname "${BASH_SOURCE[0]}")/..)"

rm -rf "$dir/build/tmp"
mkdir -p "$dir/build/tmp"
git clone -q --depth 1 https://github.com/nim-lang/csources_v1.git "$dir/build/tmp/csources"

versions=("1.2.16" "1.4.8" "1.6.2")

for version in "${versions[@]}"
do
  cd "$dir/build/tmp"
  git clone --branch "v$version" --depth 1 https://github.com/nim-lang/Nim.git "nim-$version"
  cd "nim-$version"
  cp -R "$dir/build/tmp/csources" .
  sh build_all.sh
  ./koch boot --parallelBuild:8 -d:release
  ./koch tools --parallelBuild:8 -d:release
  ./koch nimble --parallelBuild:8 -d:release
  cd "$dir/build/tmp"
  tar cvJf "nim-$version--arm64-macos-bigsur.tar.xz" \
    --exclude ".*" \
    --exclude "nim-$version/c_code" \
    --exclude "nim-$version/csources" \
    --exclude "nim-$version/csources/c_code" \
    --exclude "nim-$version/csources_v1" \
    --exclude "nim-$version/csources_v1/c_code" \
    --exclude "nim-$version/nimcache" \
    "nim-$version"
  mv "nim-$version--arm64-macos-bigsur.tar.xz" "$dir/build/"
done
