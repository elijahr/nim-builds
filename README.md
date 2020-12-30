This repository contains **unofficial** builds of the [Nim](https://nim-lang.org) compiler for various Linux distributions and CPU architectures.

The GNU builds are tested on Debian Buster, Ubuntu Bionic, Ubuntu Focal, Arch Linux, and Manjaro Linux. The musl builds are tested on Alpine Linux 3.8, 3.9, 3.10, 3.11, and 3.12. The builds are tested against a very small subset of the Nim test suite.

When new versions of Nim are released, this repository will automatically try to create and release new binaries within a few hours.

If you encounter anything unusual that doesn't seem like a bug in Nim, please report it. These builds are created for my benefit and shared for yours, with the caveat that, again, they are not official builds and they are not rigorously tested.

Pull requests targeting other architectures are welcome! This project uses distributed cross-compilers from [build-farm](https://github.com/elijahr/build-farm).


## [Nim 1.4.2](https://github.com/elijahr/nim-builds/releases/tag/nim-1.4.2--202012292139)

- [nim-1.4.2--aarch64-linux-gnu.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.4.2--202012292139/nim-1.4.2--aarch64-linux-gnu.tar.xz)

  This was compiled for the `aarch64` aka `arm64` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/arm64/v8` platform.

- [nim-1.4.2--aarch64-linux-musl.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.4.2--202012292139/nim-1.4.2--aarch64-linux-musl.tar.xz)

  This was compiled for the `aarch64` aka `arm64` architecture, for distros using the musl implementation of the C standard library, such as Alpine Linux. It can be used with Docker images targeting the `linux/arm64/v8` platform.

- [nim-1.4.2--armv5-linux-gnueabi.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.4.2--202012292139/nim-1.4.2--armv5-linux-gnueabi.tar.xz)

  This was compiled for the `armv5` aka `armel` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/arm/v5` platform.

- [nim-1.4.2--armv6-linux-musleabihf.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.4.2--202012292139/nim-1.4.2--armv6-linux-musleabihf.tar.xz)

  This was compiled for the `armv6` aka `armhf` architecture, for distros using the musl implementation of the C standard library, such as Alpine Linux. It can be used with Docker images targeting the `linux/arm/v6` platform.

- [nim-1.4.2--armv7-linux-gnueabihf.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.4.2--202012292139/nim-1.4.2--armv7-linux-gnueabihf.tar.xz)

  This was compiled for the `armv7` aka `armhf` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/arm/v7` platform.

- [nim-1.4.2--armv7-linux-musleabihf.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.4.2--202012292139/nim-1.4.2--armv7-linux-musleabihf.tar.xz)

  This was compiled for the `armv7` aka `armhf` architecture, for distros using the musl implementation of the C standard library, such as Alpine Linux. It can be used with Docker images targeting the `linux/arm/v7` platform.

- [nim-1.4.2--i686-linux-gnu.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.4.2--202012292139/nim-1.4.2--i686-linux-gnu.tar.xz)

  This was compiled for the `i686` aka `i386/i586` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/386` platform.

- [nim-1.4.2--powerpc64le-linux-gnu.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.4.2--202012292139/nim-1.4.2--powerpc64le-linux-gnu.tar.xz)

  This was compiled for the `powerpc64le` aka `ppc64le` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/ppc64le` platform.

- [nim-1.4.2--x86_64-linux-gnu.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.4.2--202012292139/nim-1.4.2--x86_64-linux-gnu.tar.xz)

  This was compiled for the `x86_64` aka `amd64` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/amd64` platform.

- [nim-1.4.2--x86_64-linux-musl.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.4.2--202012292139/nim-1.4.2--x86_64-linux-musl.tar.xz)

  This was compiled for the `x86_64` aka `amd64` architecture, for distros using the musl implementation of the C standard library, such as Alpine Linux. It can be used with Docker images targeting the `linux/amd64` platform.


## [Nim 1.4.2](https://github.com/elijahr/nim-builds/releases/tag/nim-1.4.2--202012300124)

- [nim-1.4.2--x86_64-linux-gnu.tar.xz](https://github.com/elijahr/nim-builds/releases/download/untagged-3912c316e9a47b56d9f9/nim-1.4.2--x86_64-linux-gnu.tar.xz)

  This was compiled for the `x86_64` aka `amd64` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/amd64` platform.


## [Nim 1.2.8](https://github.com/elijahr/nim-builds/releases/tag/nim-1.2.8--202012292139)

- [nim-1.2.8--aarch64-linux-gnu.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.2.8--202012292139/nim-1.2.8--aarch64-linux-gnu.tar.xz)

  This was compiled for the `aarch64` aka `arm64` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/arm64/v8` platform.

- [nim-1.2.8--aarch64-linux-musl.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.2.8--202012292139/nim-1.2.8--aarch64-linux-musl.tar.xz)

  This was compiled for the `aarch64` aka `arm64` architecture, for distros using the musl implementation of the C standard library, such as Alpine Linux. It can be used with Docker images targeting the `linux/arm64/v8` platform.

- [nim-1.2.8--armv5-linux-gnueabi.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.2.8--202012292139/nim-1.2.8--armv5-linux-gnueabi.tar.xz)

  This was compiled for the `armv5` aka `armel` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/arm/v5` platform.

- [nim-1.2.8--armv6-linux-musleabihf.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.2.8--202012292139/nim-1.2.8--armv6-linux-musleabihf.tar.xz)

  This was compiled for the `armv6` aka `armhf` architecture, for distros using the musl implementation of the C standard library, such as Alpine Linux. It can be used with Docker images targeting the `linux/arm/v6` platform.

- [nim-1.2.8--armv7-linux-gnueabihf.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.2.8--202012292139/nim-1.2.8--armv7-linux-gnueabihf.tar.xz)

  This was compiled for the `armv7` aka `armhf` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/arm/v7` platform.

- [nim-1.2.8--armv7-linux-musleabihf.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.2.8--202012292139/nim-1.2.8--armv7-linux-musleabihf.tar.xz)

  This was compiled for the `armv7` aka `armhf` architecture, for distros using the musl implementation of the C standard library, such as Alpine Linux. It can be used with Docker images targeting the `linux/arm/v7` platform.

- [nim-1.2.8--i686-linux-gnu.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.2.8--202012292139/nim-1.2.8--i686-linux-gnu.tar.xz)

  This was compiled for the `i686` aka `i386/i586` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/386` platform.

- [nim-1.2.8--powerpc64le-linux-gnu.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.2.8--202012292139/nim-1.2.8--powerpc64le-linux-gnu.tar.xz)

  This was compiled for the `powerpc64le` aka `ppc64le` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/ppc64le` platform.

- [nim-1.2.8--x86_64-linux-gnu.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.2.8--202012292139/nim-1.2.8--x86_64-linux-gnu.tar.xz)

  This was compiled for the `x86_64` aka `amd64` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/amd64` platform.

- [nim-1.2.8--x86_64-linux-musl.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.2.8--202012292139/nim-1.2.8--x86_64-linux-musl.tar.xz)

  This was compiled for the `x86_64` aka `amd64` architecture, for distros using the musl implementation of the C standard library, such as Alpine Linux. It can be used with Docker images targeting the `linux/amd64` platform.


## [Nim 1.2.8](https://github.com/elijahr/nim-builds/releases/tag/nim-1.2.8--202012300124)


## [Nim 1.0.10](https://github.com/elijahr/nim-builds/releases/tag/nim-1.0.10--202012292139)

- [nim-1.0.10--aarch64-linux-gnu.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.0.10--202012292139/nim-1.0.10--aarch64-linux-gnu.tar.xz)

  This was compiled for the `aarch64` aka `arm64` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/arm64/v8` platform.

- [nim-1.0.10--aarch64-linux-musl.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.0.10--202012292139/nim-1.0.10--aarch64-linux-musl.tar.xz)

  This was compiled for the `aarch64` aka `arm64` architecture, for distros using the musl implementation of the C standard library, such as Alpine Linux. It can be used with Docker images targeting the `linux/arm64/v8` platform.

- [nim-1.0.10--armv5-linux-gnueabi.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.0.10--202012292139/nim-1.0.10--armv5-linux-gnueabi.tar.xz)

  This was compiled for the `armv5` aka `armel` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/arm/v5` platform.

- [nim-1.0.10--armv6-linux-musleabihf.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.0.10--202012292139/nim-1.0.10--armv6-linux-musleabihf.tar.xz)

  This was compiled for the `armv6` aka `armhf` architecture, for distros using the musl implementation of the C standard library, such as Alpine Linux. It can be used with Docker images targeting the `linux/arm/v6` platform.

- [nim-1.0.10--armv7-linux-gnueabihf.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.0.10--202012292139/nim-1.0.10--armv7-linux-gnueabihf.tar.xz)

  This was compiled for the `armv7` aka `armhf` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/arm/v7` platform.

- [nim-1.0.10--armv7-linux-musleabihf.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.0.10--202012292139/nim-1.0.10--armv7-linux-musleabihf.tar.xz)

  This was compiled for the `armv7` aka `armhf` architecture, for distros using the musl implementation of the C standard library, such as Alpine Linux. It can be used with Docker images targeting the `linux/arm/v7` platform.

- [nim-1.0.10--i686-linux-gnu.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.0.10--202012292139/nim-1.0.10--i686-linux-gnu.tar.xz)

  This was compiled for the `i686` aka `i386/i586` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/386` platform.

- [nim-1.0.10--powerpc64le-linux-gnu.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.0.10--202012292139/nim-1.0.10--powerpc64le-linux-gnu.tar.xz)

  This was compiled for the `powerpc64le` aka `ppc64le` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/ppc64le` platform.

- [nim-1.0.10--x86_64-linux-gnu.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.0.10--202012292139/nim-1.0.10--x86_64-linux-gnu.tar.xz)

  This was compiled for the `x86_64` aka `amd64` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/amd64` platform.

- [nim-1.0.10--x86_64-linux-musl.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-1.0.10--202012292139/nim-1.0.10--x86_64-linux-musl.tar.xz)

  This was compiled for the `x86_64` aka `amd64` architecture, for distros using the musl implementation of the C standard library, such as Alpine Linux. It can be used with Docker images targeting the `linux/amd64` platform.


## [Nim 1.0.10](https://github.com/elijahr/nim-builds/releases/tag/nim-1.0.10--202012300124)


## [Nim 0.20.2](https://github.com/elijahr/nim-builds/releases/tag/nim-0.20.2--202012292139)

- [nim-0.20.2--aarch64-linux-gnu.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-0.20.2--202012292139/nim-0.20.2--aarch64-linux-gnu.tar.xz)

  This was compiled for the `aarch64` aka `arm64` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/arm64/v8` platform.

- [nim-0.20.2--aarch64-linux-musl.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-0.20.2--202012292139/nim-0.20.2--aarch64-linux-musl.tar.xz)

  This was compiled for the `aarch64` aka `arm64` architecture, for distros using the musl implementation of the C standard library, such as Alpine Linux. It can be used with Docker images targeting the `linux/arm64/v8` platform.

- [nim-0.20.2--armv5-linux-gnueabi.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-0.20.2--202012292139/nim-0.20.2--armv5-linux-gnueabi.tar.xz)

  This was compiled for the `armv5` aka `armel` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/arm/v5` platform.

- [nim-0.20.2--armv6-linux-musleabihf.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-0.20.2--202012292139/nim-0.20.2--armv6-linux-musleabihf.tar.xz)

  This was compiled for the `armv6` aka `armhf` architecture, for distros using the musl implementation of the C standard library, such as Alpine Linux. It can be used with Docker images targeting the `linux/arm/v6` platform.

- [nim-0.20.2--armv7-linux-gnueabihf.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-0.20.2--202012292139/nim-0.20.2--armv7-linux-gnueabihf.tar.xz)

  This was compiled for the `armv7` aka `armhf` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/arm/v7` platform.

- [nim-0.20.2--armv7-linux-musleabihf.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-0.20.2--202012292139/nim-0.20.2--armv7-linux-musleabihf.tar.xz)

  This was compiled for the `armv7` aka `armhf` architecture, for distros using the musl implementation of the C standard library, such as Alpine Linux. It can be used with Docker images targeting the `linux/arm/v7` platform.

- [nim-0.20.2--i686-linux-gnu.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-0.20.2--202012292139/nim-0.20.2--i686-linux-gnu.tar.xz)

  This was compiled for the `i686` aka `i386/i586` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/386` platform.

- [nim-0.20.2--powerpc64le-linux-gnu.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-0.20.2--202012292139/nim-0.20.2--powerpc64le-linux-gnu.tar.xz)

  This was compiled for the `powerpc64le` aka `ppc64le` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/ppc64le` platform.

- [nim-0.20.2--x86_64-linux-gnu.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-0.20.2--202012292139/nim-0.20.2--x86_64-linux-gnu.tar.xz)

  This was compiled for the `x86_64` aka `amd64` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/amd64` platform.

- [nim-0.20.2--x86_64-linux-musl.tar.xz](https://github.com/elijahr/nim-builds/releases/download/nim-0.20.2--202012292139/nim-0.20.2--x86_64-linux-musl.tar.xz)

  This was compiled for the `x86_64` aka `amd64` architecture, for distros using the musl implementation of the C standard library, such as Alpine Linux. It can be used with Docker images targeting the `linux/amd64` platform.


## [Nim 0.20.2](https://github.com/elijahr/nim-builds/releases/tag/nim-0.20.2--202012300124)

- [nim-0.20.2--x86_64-linux-gnu.tar.xz](https://github.com/elijahr/nim-builds/releases/download/untagged-61b1ec4f002c62876728/nim-0.20.2--x86_64-linux-gnu.tar.xz)

  This was compiled for the `x86_64` aka `amd64` architecture, for distros using the GNU implementation of the C standard library, such as Debian, Ubuntu, Arch Linux, and Manjaro. It can be used with Docker images targeting the `linux/amd64` platform.

