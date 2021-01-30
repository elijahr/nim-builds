#!/bin/sh

cd build

git clone --branch v1.0.10 --depth 1 https://github.com/nim-lang/Nim.git nim-1.0.10
git clone --branch v1.2.8 --depth 1 https://github.com/nim-lang/Nim.git nim-1.2.8
git clone --branch v1.4.2 --depth 1 https://github.com/nim-lang/Nim.git nim-1.4.2

git clone -q --depth 1 https://github.com/nim-lang/csources_v1.git csources

cp -R csources nim-1.0.10/
cp -R csources nim-1.2.8/
cp -R csources nim-1.4.2/

tar cvJf nim-1.0.10--arm64-macos-bigsur.tar.xz --exclude ".*" --exclude "./csources" --exclude "./nimcache" nim-1.0.10
tar cvJf nim-1.2.8--arm64-macos-bigsur.tar.xz --exclude ".*" --exclude "./csources" --exclude "./nimcache" nim-1.2.8
tar cvJf nim-1.4.2--arm64-macos-bigsur.tar.xz --exclude ".*" --exclude "./csources" --exclude "./nimcache" nim-1.4.2
