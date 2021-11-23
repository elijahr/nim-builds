# Hello!

This repository contains unofficial builds of [Nim](https://nim-lang.org) for various operating systems and CPU architectures (armv5, armv6, armv7, arm64, amd64, i686, powerpc64le).

These builds are created and shared for the benefit of the community, with the caveat that they are not rigorously tested.

When new versions of Nim are released, this repository will automatically try to create and release new binaries within a few hours.

## Linux

The GNU builds are tested on Debian, Ubuntu, Fedora, Arch, and Manjaro.

The musl builds are tested on Alpine.

The builds are tested against a very small subset of Nim's test suite.

## macOS

The x86_64 macOS builds are tested on Big Sur 11.0 and Catalina 10.15.
The arm64 macOS builds are untested.

## [Nim 1.6.0](https://github.com/elijahr/nim-builds/releases/tag/nim-1.6.0--202111230013)

Built: 2021-11-23


- [nim-1.6.0--aarch64-linux-gnu.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.6.0--202111230013/nim-1.6.0--aarch64-linux-gnu.tar.xz)

  This was compiled for the `aarch64` aka `arm64` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Fedora, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/arm64/v8` platform.

- [nim-1.6.0--aarch64-linux-musl.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.6.0--202111230013/nim-1.6.0--aarch64-linux-musl.tar.xz)

  This was compiled for the `aarch64` aka `arm64` architecture, for distros using the musl implementation of the C standard library, such as Alpine Linux. It can be used with Docker images targeting the `linux/arm64/v8` platform.

- [nim-1.6.0--arm64-macos-bigsur.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.6.0--202111230013/nim-1.6.0--arm64-macos-bigsur.tar.xz)

  This was compiled on macOS Big Sur 11.0 for the `arm64` architecture.

- [nim-1.6.0--armv5-linux-gnueabi.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.6.0--202111230013/nim-1.6.0--armv5-linux-gnueabi.tar.xz)

  This was compiled for the `armv5` aka `armel` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Fedora, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/arm/v5` platform.

- [nim-1.6.0--armv6-linux-musleabihf.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.6.0--202111230013/nim-1.6.0--armv6-linux-musleabihf.tar.xz)

  This was compiled for the `armv6` architecture, for distros using the musl implementation of the C standard library, such as Alpine Linux. It can be used with Docker images targeting the `linux/arm/v6` platform.

- [nim-1.6.0--armv7-linux-gnueabihf.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.6.0--202111230013/nim-1.6.0--armv7-linux-gnueabihf.tar.xz)

  This was compiled for the `armv7` aka `armhf` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Fedora, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/arm/v7` platform.

- [nim-1.6.0--armv7-linux-musleabihf.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.6.0--202111230013/nim-1.6.0--armv7-linux-musleabihf.tar.xz)

  This was compiled for the `armv7` aka `armhf` architecture, for distros using the musl implementation of the C standard library, such as Alpine Linux. It can be used with Docker images targeting the `linux/arm/v7` platform.

- [nim-1.6.0--i686-linux-gnu.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.6.0--202111230013/nim-1.6.0--i686-linux-gnu.tar.xz)

  This was compiled for the `i686` aka `x86` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Fedora, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/386` platform.

- [nim-1.6.0--powerpc64le-linux-gnu.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.6.0--202111230013/nim-1.6.0--powerpc64le-linux-gnu.tar.xz)

  This was compiled for the `powerpc64le` aka `ppc64le` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Fedora, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/ppc64le` platform.

- [nim-1.6.0--x86_64-linux-gnu.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.6.0--202111230013/nim-1.6.0--x86_64-linux-gnu.tar.xz)

  This was compiled for the `x86_64` aka `amd64` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Fedora, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/amd64` platform.

- [nim-1.6.0--x86_64-linux-musl.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.6.0--202111230013/nim-1.6.0--x86_64-linux-musl.tar.xz)

  This was compiled for the `x86_64` aka `amd64` architecture, for distros using the musl implementation of the C standard library, such as Alpine Linux. It can be used with Docker images targeting the `linux/amd64` platform.

- [nim-1.6.0--x86_64-macos-bigsur.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.6.0--202111230013/nim-1.6.0--x86_64-macos-bigsur.tar.xz)

  This was compiled on macOS Big Sur 11.0 for the `x86_64` architecture.

- [nim-1.6.0--x86_64-macos-catalina.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.6.0--202111230013/nim-1.6.0--x86_64-macos-catalina.tar.xz)

  This was compiled on macOS Catalina 10.15 for the `x86_64` architecture.


## [Nim 1.4.8](https://github.com/elijahr/nim-builds/releases/tag/nim-1.4.8--202111230013)

Built: 2021-11-23


- [nim-1.4.8--aarch64-linux-gnu.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.4.8--202111230013/nim-1.4.8--aarch64-linux-gnu.tar.xz)

  This was compiled for the `aarch64` aka `arm64` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Fedora, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/arm64/v8` platform.

- [nim-1.4.8--aarch64-linux-musl.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.4.8--202111230013/nim-1.4.8--aarch64-linux-musl.tar.xz)

  This was compiled for the `aarch64` aka `arm64` architecture, for distros using the musl implementation of the C standard library, such as Alpine Linux. It can be used with Docker images targeting the `linux/arm64/v8` platform.

- [nim-1.4.8--arm64-macos-bigsur.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.4.8--202111230013/nim-1.4.8--arm64-macos-bigsur.tar.xz)

  This was compiled on macOS Big Sur 11.0 for the `arm64` architecture.

- [nim-1.4.8--armv5-linux-gnueabi.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.4.8--202111230013/nim-1.4.8--armv5-linux-gnueabi.tar.xz)

  This was compiled for the `armv5` aka `armel` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Fedora, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/arm/v5` platform.

- [nim-1.4.8--armv6-linux-musleabihf.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.4.8--202111230013/nim-1.4.8--armv6-linux-musleabihf.tar.xz)

  This was compiled for the `armv6` architecture, for distros using the musl implementation of the C standard library, such as Alpine Linux. It can be used with Docker images targeting the `linux/arm/v6` platform.

- [nim-1.4.8--armv7-linux-gnueabihf.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.4.8--202111230013/nim-1.4.8--armv7-linux-gnueabihf.tar.xz)

  This was compiled for the `armv7` aka `armhf` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Fedora, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/arm/v7` platform.

- [nim-1.4.8--armv7-linux-musleabihf.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.4.8--202111230013/nim-1.4.8--armv7-linux-musleabihf.tar.xz)

  This was compiled for the `armv7` aka `armhf` architecture, for distros using the musl implementation of the C standard library, such as Alpine Linux. It can be used with Docker images targeting the `linux/arm/v7` platform.

- [nim-1.4.8--i686-linux-gnu.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.4.8--202111230013/nim-1.4.8--i686-linux-gnu.tar.xz)

  This was compiled for the `i686` aka `x86` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Fedora, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/386` platform.

- [nim-1.4.8--powerpc64le-linux-gnu.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.4.8--202111230013/nim-1.4.8--powerpc64le-linux-gnu.tar.xz)

  This was compiled for the `powerpc64le` aka `ppc64le` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Fedora, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/ppc64le` platform.

- [nim-1.4.8--x86_64-linux-gnu.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.4.8--202111230013/nim-1.4.8--x86_64-linux-gnu.tar.xz)

  This was compiled for the `x86_64` aka `amd64` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Fedora, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/amd64` platform.

- [nim-1.4.8--x86_64-linux-musl.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.4.8--202111230013/nim-1.4.8--x86_64-linux-musl.tar.xz)

  This was compiled for the `x86_64` aka `amd64` architecture, for distros using the musl implementation of the C standard library, such as Alpine Linux. It can be used with Docker images targeting the `linux/amd64` platform.

- [nim-1.4.8--x86_64-macos-bigsur.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.4.8--202111230013/nim-1.4.8--x86_64-macos-bigsur.tar.xz)

  This was compiled on macOS Big Sur 11.0 for the `x86_64` architecture.

- [nim-1.4.8--x86_64-macos-catalina.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.4.8--202111230013/nim-1.4.8--x86_64-macos-catalina.tar.xz)

  This was compiled on macOS Catalina 10.15 for the `x86_64` architecture.


## [Nim 1.4.2](https://github.com/elijahr/nim-builds/releases/tag/nim-1.4.2--202101302308)

Built: 2021-01-30


- [nim-1.4.2--aarch64-linux-gnu.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.4.2--202101302308/nim-1.4.2--aarch64-linux-gnu.tar.xz)

  This was compiled for the `aarch64` aka `arm64` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Fedora, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/arm64/v8` platform.

- [nim-1.4.2--aarch64-linux-musl.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.4.2--202101302308/nim-1.4.2--aarch64-linux-musl.tar.xz)

  This was compiled for the `aarch64` aka `arm64` architecture, for distros using the musl implementation of the C standard library, such as Alpine Linux. It can be used with Docker images targeting the `linux/arm64/v8` platform.

- [nim-1.4.2--arm64-macos-bigsur.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.4.2--202101302308/nim-1.4.2--arm64-macos-bigsur.tar.xz)

  This was compiled on macOS Big Sur 11.0 for the `arm64` architecture.

- [nim-1.4.2--armv5-linux-gnueabi.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.4.2--202101302308/nim-1.4.2--armv5-linux-gnueabi.tar.xz)

  This was compiled for the `armv5` aka `armel` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Fedora, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/arm/v5` platform.

- [nim-1.4.2--armv6-linux-musleabihf.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.4.2--202101302308/nim-1.4.2--armv6-linux-musleabihf.tar.xz)

  This was compiled for the `armv6` architecture, for distros using the musl implementation of the C standard library, such as Alpine Linux. It can be used with Docker images targeting the `linux/arm/v6` platform.

- [nim-1.4.2--armv7-linux-gnueabihf.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.4.2--202101302308/nim-1.4.2--armv7-linux-gnueabihf.tar.xz)

  This was compiled for the `armv7` aka `armhf` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Fedora, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/arm/v7` platform.

- [nim-1.4.2--armv7-linux-musleabihf.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.4.2--202101302308/nim-1.4.2--armv7-linux-musleabihf.tar.xz)

  This was compiled for the `armv7` aka `armhf` architecture, for distros using the musl implementation of the C standard library, such as Alpine Linux. It can be used with Docker images targeting the `linux/arm/v7` platform.

- [nim-1.4.2--i686-linux-gnu.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.4.2--202101302308/nim-1.4.2--i686-linux-gnu.tar.xz)

  This was compiled for the `i686` aka `x86` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Fedora, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/386` platform.

- [nim-1.4.2--powerpc64le-linux-gnu.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.4.2--202101302308/nim-1.4.2--powerpc64le-linux-gnu.tar.xz)

  This was compiled for the `powerpc64le` aka `ppc64le` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Fedora, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/ppc64le` platform.

- [nim-1.4.2--x86_64-linux-gnu.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.4.2--202101302308/nim-1.4.2--x86_64-linux-gnu.tar.xz)

  This was compiled for the `x86_64` aka `amd64` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Fedora, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/amd64` platform.

- [nim-1.4.2--x86_64-linux-musl.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.4.2--202101302308/nim-1.4.2--x86_64-linux-musl.tar.xz)

  This was compiled for the `x86_64` aka `amd64` architecture, for distros using the musl implementation of the C standard library, such as Alpine Linux. It can be used with Docker images targeting the `linux/amd64` platform.

- [nim-1.4.2--x86_64-macos-bigsur.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.4.2--202101302308/nim-1.4.2--x86_64-macos-bigsur.tar.xz)

  This was compiled on macOS Big Sur 11.0 for the `x86_64` architecture.

- [nim-1.4.2--x86_64-macos-catalina.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.4.2--202101302308/nim-1.4.2--x86_64-macos-catalina.tar.xz)

  This was compiled on macOS Catalina 10.15 for the `x86_64` architecture.


## [Nim 1.2.12](https://github.com/elijahr/nim-builds/releases/tag/nim-1.2.12--202111230013)

Built: 2021-11-23


- [nim-1.2.12--aarch64-linux-gnu.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.2.12--202111230013/nim-1.2.12--aarch64-linux-gnu.tar.xz)

  This was compiled for the `aarch64` aka `arm64` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Fedora, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/arm64/v8` platform.

- [nim-1.2.12--aarch64-linux-musl.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.2.12--202111230013/nim-1.2.12--aarch64-linux-musl.tar.xz)

  This was compiled for the `aarch64` aka `arm64` architecture, for distros using the musl implementation of the C standard library, such as Alpine Linux. It can be used with Docker images targeting the `linux/arm64/v8` platform.

- [nim-1.2.12--armv5-linux-gnueabi.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.2.12--202111230013/nim-1.2.12--armv5-linux-gnueabi.tar.xz)

  This was compiled for the `armv5` aka `armel` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Fedora, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/arm/v5` platform.

- [nim-1.2.12--armv6-linux-musleabihf.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.2.12--202111230013/nim-1.2.12--armv6-linux-musleabihf.tar.xz)

  This was compiled for the `armv6` architecture, for distros using the musl implementation of the C standard library, such as Alpine Linux. It can be used with Docker images targeting the `linux/arm/v6` platform.

- [nim-1.2.12--armv7-linux-gnueabihf.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.2.12--202111230013/nim-1.2.12--armv7-linux-gnueabihf.tar.xz)

  This was compiled for the `armv7` aka `armhf` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Fedora, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/arm/v7` platform.

- [nim-1.2.12--armv7-linux-musleabihf.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.2.12--202111230013/nim-1.2.12--armv7-linux-musleabihf.tar.xz)

  This was compiled for the `armv7` aka `armhf` architecture, for distros using the musl implementation of the C standard library, such as Alpine Linux. It can be used with Docker images targeting the `linux/arm/v7` platform.

- [nim-1.2.12--i686-linux-gnu.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.2.12--202111230013/nim-1.2.12--i686-linux-gnu.tar.xz)

  This was compiled for the `i686` aka `x86` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Fedora, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/386` platform.

- [nim-1.2.12--powerpc64le-linux-gnu.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.2.12--202111230013/nim-1.2.12--powerpc64le-linux-gnu.tar.xz)

  This was compiled for the `powerpc64le` aka `ppc64le` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Fedora, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/ppc64le` platform.

- [nim-1.2.12--x86_64-linux-gnu.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.2.12--202111230013/nim-1.2.12--x86_64-linux-gnu.tar.xz)

  This was compiled for the `x86_64` aka `amd64` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Fedora, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/amd64` platform.

- [nim-1.2.12--x86_64-linux-musl.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.2.12--202111230013/nim-1.2.12--x86_64-linux-musl.tar.xz)

  This was compiled for the `x86_64` aka `amd64` architecture, for distros using the musl implementation of the C standard library, such as Alpine Linux. It can be used with Docker images targeting the `linux/amd64` platform.

- [nim-1.2.12--x86_64-macos-bigsur.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.2.12--202111230013/nim-1.2.12--x86_64-macos-bigsur.tar.xz)

  This was compiled on macOS Big Sur 11.0 for the `x86_64` architecture.

- [nim-1.2.12--x86_64-macos-catalina.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.2.12--202111230013/nim-1.2.12--x86_64-macos-catalina.tar.xz)

  This was compiled on macOS Catalina 10.15 for the `x86_64` architecture.


## [Nim 1.2.8](https://github.com/elijahr/nim-builds/releases/tag/nim-1.2.8--202101302308)

Built: 2021-01-30


- [nim-1.2.8--aarch64-linux-gnu.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.2.8--202101302308/nim-1.2.8--aarch64-linux-gnu.tar.xz)

  This was compiled for the `aarch64` aka `arm64` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Fedora, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/arm64/v8` platform.

- [nim-1.2.8--aarch64-linux-musl.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.2.8--202101302308/nim-1.2.8--aarch64-linux-musl.tar.xz)

  This was compiled for the `aarch64` aka `arm64` architecture, for distros using the musl implementation of the C standard library, such as Alpine Linux. It can be used with Docker images targeting the `linux/arm64/v8` platform.

- [nim-1.2.8--arm64-macos-bigsur.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.2.8--202101302308/nim-1.2.8--arm64-macos-bigsur.tar.xz)

  This was compiled on macOS Big Sur 11.0 for the `arm64` architecture.

- [nim-1.2.8--armv5-linux-gnueabi.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.2.8--202101302308/nim-1.2.8--armv5-linux-gnueabi.tar.xz)

  This was compiled for the `armv5` aka `armel` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Fedora, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/arm/v5` platform.

- [nim-1.2.8--armv6-linux-musleabihf.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.2.8--202101302308/nim-1.2.8--armv6-linux-musleabihf.tar.xz)

  This was compiled for the `armv6` architecture, for distros using the musl implementation of the C standard library, such as Alpine Linux. It can be used with Docker images targeting the `linux/arm/v6` platform.

- [nim-1.2.8--armv7-linux-gnueabihf.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.2.8--202101302308/nim-1.2.8--armv7-linux-gnueabihf.tar.xz)

  This was compiled for the `armv7` aka `armhf` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Fedora, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/arm/v7` platform.

- [nim-1.2.8--armv7-linux-musleabihf.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.2.8--202101302308/nim-1.2.8--armv7-linux-musleabihf.tar.xz)

  This was compiled for the `armv7` aka `armhf` architecture, for distros using the musl implementation of the C standard library, such as Alpine Linux. It can be used with Docker images targeting the `linux/arm/v7` platform.

- [nim-1.2.8--i686-linux-gnu.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.2.8--202101302308/nim-1.2.8--i686-linux-gnu.tar.xz)

  This was compiled for the `i686` aka `x86` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Fedora, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/386` platform.

- [nim-1.2.8--powerpc64le-linux-gnu.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.2.8--202101302308/nim-1.2.8--powerpc64le-linux-gnu.tar.xz)

  This was compiled for the `powerpc64le` aka `ppc64le` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Fedora, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/ppc64le` platform.

- [nim-1.2.8--x86_64-linux-gnu.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.2.8--202101302308/nim-1.2.8--x86_64-linux-gnu.tar.xz)

  This was compiled for the `x86_64` aka `amd64` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Fedora, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/amd64` platform.

- [nim-1.2.8--x86_64-linux-musl.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.2.8--202101302308/nim-1.2.8--x86_64-linux-musl.tar.xz)

  This was compiled for the `x86_64` aka `amd64` architecture, for distros using the musl implementation of the C standard library, such as Alpine Linux. It can be used with Docker images targeting the `linux/amd64` platform.

- [nim-1.2.8--x86_64-macos-bigsur.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.2.8--202101302308/nim-1.2.8--x86_64-macos-bigsur.tar.xz)

  This was compiled on macOS Big Sur 11.0 for the `x86_64` architecture.

- [nim-1.2.8--x86_64-macos-catalina.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.2.8--202101302308/nim-1.2.8--x86_64-macos-catalina.tar.xz)

  This was compiled on macOS Catalina 10.15 for the `x86_64` architecture.


## [Nim 1.0.10](https://github.com/elijahr/nim-builds/releases/tag/nim-1.0.10--202101302308)

Built: 2021-01-30


- [nim-1.0.10--aarch64-linux-gnu.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.0.10--202101302308/nim-1.0.10--aarch64-linux-gnu.tar.xz)

  This was compiled for the `aarch64` aka `arm64` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Fedora, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/arm64/v8` platform.

- [nim-1.0.10--aarch64-linux-musl.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.0.10--202101302308/nim-1.0.10--aarch64-linux-musl.tar.xz)

  This was compiled for the `aarch64` aka `arm64` architecture, for distros using the musl implementation of the C standard library, such as Alpine Linux. It can be used with Docker images targeting the `linux/arm64/v8` platform.

- [nim-1.0.10--arm64-macos-bigsur.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.0.10--202101302308/nim-1.0.10--arm64-macos-bigsur.tar.xz)

  This was compiled on macOS Big Sur 11.0 for the `arm64` architecture.

- [nim-1.0.10--armv5-linux-gnueabi.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.0.10--202101302308/nim-1.0.10--armv5-linux-gnueabi.tar.xz)

  This was compiled for the `armv5` aka `armel` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Fedora, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/arm/v5` platform.

- [nim-1.0.10--armv6-linux-musleabihf.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.0.10--202101302308/nim-1.0.10--armv6-linux-musleabihf.tar.xz)

  This was compiled for the `armv6` architecture, for distros using the musl implementation of the C standard library, such as Alpine Linux. It can be used with Docker images targeting the `linux/arm/v6` platform.

- [nim-1.0.10--armv7-linux-gnueabihf.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.0.10--202101302308/nim-1.0.10--armv7-linux-gnueabihf.tar.xz)

  This was compiled for the `armv7` aka `armhf` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Fedora, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/arm/v7` platform.

- [nim-1.0.10--armv7-linux-musleabihf.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.0.10--202101302308/nim-1.0.10--armv7-linux-musleabihf.tar.xz)

  This was compiled for the `armv7` aka `armhf` architecture, for distros using the musl implementation of the C standard library, such as Alpine Linux. It can be used with Docker images targeting the `linux/arm/v7` platform.

- [nim-1.0.10--i686-linux-gnu.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.0.10--202101302308/nim-1.0.10--i686-linux-gnu.tar.xz)

  This was compiled for the `i686` aka `x86` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Fedora, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/386` platform.

- [nim-1.0.10--powerpc64le-linux-gnu.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.0.10--202101302308/nim-1.0.10--powerpc64le-linux-gnu.tar.xz)

  This was compiled for the `powerpc64le` aka `ppc64le` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Fedora, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/ppc64le` platform.

- [nim-1.0.10--x86_64-linux-gnu.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.0.10--202101302308/nim-1.0.10--x86_64-linux-gnu.tar.xz)

  This was compiled for the `x86_64` aka `amd64` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Fedora, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/amd64` platform.

- [nim-1.0.10--x86_64-linux-musl.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.0.10--202101302308/nim-1.0.10--x86_64-linux-musl.tar.xz)

  This was compiled for the `x86_64` aka `amd64` architecture, for distros using the musl implementation of the C standard library, such as Alpine Linux. It can be used with Docker images targeting the `linux/amd64` platform.

- [nim-1.0.10--x86_64-macos-bigsur.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.0.10--202101302308/nim-1.0.10--x86_64-macos-bigsur.tar.xz)

  This was compiled on macOS Big Sur 11.0 for the `x86_64` architecture.

- [nim-1.0.10--x86_64-macos-catalina.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.0.10--202101302308/nim-1.0.10--x86_64-macos-catalina.tar.xz)

  This was compiled on macOS Catalina 10.15 for the `x86_64` architecture.


## [Nim 0.20.2](https://github.com/elijahr/nim-builds/releases/tag/nim-0.20.2--202101302307)

Built: 2021-01-30


- [nim-0.20.2--aarch64-linux-gnu.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-0.20.2--202101302307/nim-0.20.2--aarch64-linux-gnu.tar.xz)

  This was compiled for the `aarch64` aka `arm64` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Fedora, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/arm64/v8` platform.

- [nim-0.20.2--aarch64-linux-musl.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-0.20.2--202101302307/nim-0.20.2--aarch64-linux-musl.tar.xz)

  This was compiled for the `aarch64` aka `arm64` architecture, for distros using the musl implementation of the C standard library, such as Alpine Linux. It can be used with Docker images targeting the `linux/arm64/v8` platform.

- [nim-0.20.2--armv5-linux-gnueabi.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-0.20.2--202101302307/nim-0.20.2--armv5-linux-gnueabi.tar.xz)

  This was compiled for the `armv5` aka `armel` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Fedora, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/arm/v5` platform.

- [nim-0.20.2--armv6-linux-musleabihf.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-0.20.2--202101302307/nim-0.20.2--armv6-linux-musleabihf.tar.xz)

  This was compiled for the `armv6` architecture, for distros using the musl implementation of the C standard library, such as Alpine Linux. It can be used with Docker images targeting the `linux/arm/v6` platform.

- [nim-0.20.2--armv7-linux-gnueabihf.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-0.20.2--202101302307/nim-0.20.2--armv7-linux-gnueabihf.tar.xz)

  This was compiled for the `armv7` aka `armhf` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Fedora, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/arm/v7` platform.

- [nim-0.20.2--armv7-linux-musleabihf.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-0.20.2--202101302307/nim-0.20.2--armv7-linux-musleabihf.tar.xz)

  This was compiled for the `armv7` aka `armhf` architecture, for distros using the musl implementation of the C standard library, such as Alpine Linux. It can be used with Docker images targeting the `linux/arm/v7` platform.

- [nim-0.20.2--i686-linux-gnu.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-0.20.2--202101302307/nim-0.20.2--i686-linux-gnu.tar.xz)

  This was compiled for the `i686` aka `x86` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Fedora, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/386` platform.

- [nim-0.20.2--powerpc64le-linux-gnu.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-0.20.2--202101302307/nim-0.20.2--powerpc64le-linux-gnu.tar.xz)

  This was compiled for the `powerpc64le` aka `ppc64le` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Fedora, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/ppc64le` platform.

- [nim-0.20.2--x86_64-linux-gnu.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-0.20.2--202101302307/nim-0.20.2--x86_64-linux-gnu.tar.xz)

  This was compiled for the `x86_64` aka `amd64` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Fedora, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/amd64` platform.

- [nim-0.20.2--x86_64-linux-musl.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-0.20.2--202101302307/nim-0.20.2--x86_64-linux-musl.tar.xz)

  This was compiled for the `x86_64` aka `amd64` architecture, for distros using the musl implementation of the C standard library, such as Alpine Linux. It can be used with Docker images targeting the `linux/amd64` platform.

- [nim-0.20.2--x86_64-macos-bigsur.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-0.20.2--202101302307/nim-0.20.2--x86_64-macos-bigsur.tar.xz)

  This was compiled on macOS Big Sur 11.0 for the `x86_64` architecture.

- [nim-0.20.2--x86_64-macos-catalina.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-0.20.2--202101302307/nim-0.20.2--x86_64-macos-catalina.tar.xz)

  This was compiled on macOS Catalina 10.15 for the `x86_64` architecture.



## Contributing

Pull requests targeting other platforms are welcome! This project uses distributed cross-compilers from [build-farm](https://github.com/elijahr/build-farm) - start there.