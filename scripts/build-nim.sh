#!/bin/sh

set -uex

nim_dir="$1"
build_args="${2:-}"
koch_args="${3:-}"

cd "${nim_dir}"

if [ -f "build.sh" ]; then
  sh build.sh $build_args
else
  rm -rf csources
  # latest csources - macOS arm64 compatible
  git clone --depth 1 https://github.com/nim-lang/csources_v1.git csources
  (
    cd csources
    sh build.sh $build_args
  )
fi

./bin/nim c --skipUserCfg --skipParentCfg koch
./koch boot -d:release --skipUserCfg --skipParentCfg $koch_args
./koch tools --skipUserCfg --skipParentCfg $koch_args # Compile Nimble and other tools.
