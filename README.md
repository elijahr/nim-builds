# Hello!

This repository contains unofficial builds of [Nim](https://nim-lang.org) for various operating systems and CPU architectures (armv5, armv6, armv7, arm64, amd64, i686, powerpc64le).

These builds are created and shared for the benefit of the community, with the caveat that they are not rigorously tested.

When new versions of Nim are released, this repository will automatically try to create and release new binaries within a few hours.

## Linux

The GNU builds are tested on Debian, Ubuntu, Fedora, Arch, and Manjaro.

The musl builds are tested on Alpine.

The builds are tested against a very small subset of Nim's test suite.

## macOS

The macOS builds are tested on Big Sur 11.0 and Catalina 10.15.



## Contributing

Pull requests targeting other platforms are welcome! This project uses distributed cross-compilers from [build-farm](https://github.com/elijahr/build-farm) - start there.