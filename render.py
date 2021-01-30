#!/usr/bin/env python

import argparse
import datetime
import json
import os
import re
import sys

from ghapi.all import GhApi
from itertools import groupby
from jinja2 import Environment, StrictUndefined
from path import Path
from ruamel import yaml
from semver import VersionInfo


github = GhApi()


class Dumper(yaml.RoundTripDumper):
    def ignore_aliases(self, data):
        # Strip aliases
        return True


def interpolate_yaml(yaml_path):
    with open(yaml_path, "r") as f:
        rendered = yaml.load(f, Loader=yaml.RoundTripLoader)

    # Remove _anchors section
    if "_anchors" in rendered:
        del rendered["_anchors"]

    # Use custom Dumper that replaces aliases with referenced content
    rendered = yaml.dump(rendered, Dumper=Dumper)

    with open(yaml_path, "w") as f:
        f.write(rendered)

    print(f"Interpolated {yaml_path}")
    return yaml_path


project_dir = Path(os.path.dirname(os.path.abspath(__file__)))
min_version = VersionInfo.parse("0.20.2")


def slugify(string, delim="-", allowed_chars=""):
    return re.sub(r"[^\w%s]" % re.escape(allowed_chars), delim, string).lower()


def find_max_nim_versions(versions):
    versions = (VersionInfo.parse(v.strip()) for v in versions)
    versions = (v for v in versions if v >= min_version)
    for key, versions in groupby(sorted(versions), lambda v: f"{v.major}.{v.minor}"):
        yield str(max(versions))


def fetch_nim_versions():
    tags = github.repos.list_tags("nim-lang", "Nim")
    return [tag.name[1:] for tag in tags if tag.name.startswith("v")]


toolchain_arch_by_docker_arch = {
    "linux/amd64": "x86_64",
    "linux/386": "i686",
    "linux/arm/v5": "armv5",
    "linux/arm/v6": "armv6",
    "linux/arm/v7": "armv7",
    "linux/arm64/v8": "aarch64",
    "linux/ppc64le": "powerpc64le",
}

toolchain_suffix_by_docker_arch = {
    "linux/arm/v5": "eabi",
    "linux/arm/v6": "eabihf",
    "linux/arm/v7": "eabihf",
}

docker_arch_by_toolchain_arch = {v: k for k, v in toolchain_arch_by_docker_arch.items()}

toolchain_arch_aliases = {
    "x86_64": "amd64",
    "i686": "x86",
    "armv5": "armel",
    "armv7": "armhf",
    "aarch64": "arm64",
    "powerpc64le": "ppc64le",
}


def asset_blurb(asset):
    toolchain = asset["name"].split("--")[1]
    arch, os_type, tail = toolchain.split("-")
    if os_type == "linux":
        if tail.startswith("gnu"):
            libc_name = "GNU"
            libc_distros = "Debian, Ubuntu, Fedora, Arch Linux, and Manjaro"
        elif tail.startswith("musl"):
            libc_name = "musl"
            libc_distros = "Alpine Linux"
        else:
            raise ValueError(f"Unknown libc {tail}")

        if arch in toolchain_arch_aliases:
            aka = f" aka `{toolchain_arch_aliases[arch]}`"
        else:
            aka = ""

        blurb = f"This was compiled for the `{arch}`{aka} architecture, "
        blurb += f"for distros using the {libc_name} implementation of "
        blurb += f"the C standard library, such as {libc_distros}. "
        blurb += "It can be used with Docker images targeting the "
        blurb += f"`{docker_arch_by_toolchain_arch[arch]}` platform."
        return blurb

    elif os_type == "macos":
        release_name = {
            "bigsur": "Big Sur 11.0",
            "catalina": "Catalina 10.15",
        }[tail]
        blurb = f"This was compiled on macOS {release_name}."
        return blurb

    else:
        raise ValueError(f"Unknown OS {os_type}")


def machine(distro, platform):
    if distro["type"] == "linux":
        prefix = toolchain_arch_by_docker_arch[platform]
        suffix = toolchain_suffix_by_docker_arch.get(platform, "")
        return f'{prefix}-linux-{distro["libc"]}{suffix}'
    elif distro["type"] == "macos":
        return f"{platform}-macos-{distro['name']}"
    raise ValueError(f'Invalid distro type {distro["type"]}')


def id(distro, platform):
    return slugify(f"{distro['name']}-{platform}")


def asset_name(nim_version, distro, platform):
    return f"{nim_version}--{machine(distro, platform)}"


linux_distros = [
    {
        "name": "alpine-3-12",
        "type": "linux",
        "libc": "musl",
        "build_farm_host_image": "elijahru/build-farm:alpine-3.12",
        "build_farm_client_image": "elijahru/build-farm-client:alpine-3.12",
        "platforms": [
            "linux/amd64",
            "linux/arm/v6",
            "linux/arm/v7",
            "linux/arm64/v8",
        ],
        "test_targets": {
            "alpine:3.12": {
                "linux/amd64": "linux/amd64",
                "linux/arm/v6": "linux/arm/v6",
                "linux/arm/v7": "linux/arm/v7",
                "linux/arm64/v8": "linux/arm64/v8",
            },
            "alpine:3.11": {
                "linux/amd64": "linux/amd64",
            },
            "alpine:3.10": {
                "linux/amd64": "linux/amd64",
            },
            "alpine:3.9": {
                "linux/amd64": "linux/amd64",
            },
            "alpine:3.8": {
                "linux/amd64": "linux/amd64",
            },
        },
    },
    {
        "name": "debian-buster",
        "type": "linux",
        "libc": "gnu",
        "build_farm_host_image": "elijahru/build-farm:debian-buster-slim",
        "build_farm_client_image": "elijahru/build-farm-client:debian-buster-slim",
        "platforms": [
            "linux/amd64",
            "linux/386",
            "linux/arm/v5",
            "linux/arm/v7",
            "linux/arm64/v8",
            "linux/ppc64le",
        ],
        "test_targets": {
            "debian:buster-slim": {
                "linux/amd64": "linux/amd64",
                "linux/386": "linux/386",
                "linux/arm/v5": "linux/arm/v5",
                "linux/arm/v7": "linux/arm/v7",
                "linux/arm64/v8": "linux/arm64/v8",
                "linux/ppc64le": "linux/ppc64le",
            },
            "archlinux": {
                "linux/amd64": "linux/amd64",
            },
            "lopsided/archlinux": {
                "linux/arm/v5": "linux/arm/v5",
                "linux/arm/v6": "linux/arm/v6",
                "linux/arm/v7": "linux/arm/v7",
                "linux/arm64/v8": "linux/arm64/v8",
            },
            "abyo/manjaro_aarch64": {
                "linux/arm64/v8": "linux/arm64",
            },
            "ubuntu:bionic": {
                "linux/amd64": "linux/amd64",
            },
            "ubuntu:focal": {
                "linux/amd64": "linux/amd64",
            },
            "fedora:31": {
                "linux/amd64": "linux/amd64",
            },
            "fedora:32": {
                "linux/amd64": "linux/amd64",
            },
            "fedora:33": {
                "linux/amd64": "linux/amd64",
            },
        },
    },
]

macos_distros = [
    {
        "name": "catalina",
        "type": "macos",
        "runner": "macos-10.15",
        "archs": [
            "x86_64",
        ],
        "test_runners": [
            "macos-11.0",
            "macos-10.15",
        ],
    },
    {
        "name": "bigsur",
        "type": "macos",
        "runner": "macos-11.0",
        "archs": [
            "x86_64",
            # "arm64",
        ],
        "test_runners": [
            "macos-11.0",
            # "macos-10.15",
        ],
    },
]


env = Environment(autoescape=False, undefined=StrictUndefined)
env.filters["slugify"] = slugify
env.filters["asset_blurb"] = asset_blurb


def render(template, path, context):
    with project_dir:
        with open(template, "r") as f:
            rendered = env.from_string(f.read()).render(**context)
        with open(path, "w") as f:
            f.write(rendered)
        print(f"Rendered {template} -> {path}")
        if path.endswith(".yml"):
            interpolate_yaml(path)


def render_github_workflow(nim_version):
    render(
        ".github/workflows/build.yml.jinja",
        f".github/workflows/build-nim-{slugify(nim_version)}.yml",
        dict(
            linux_distros=linux_distros,
            macos_distros=macos_distros,
            nim_version=nim_version,
            slugify=slugify,
            id=id,
            asset_name=asset_name,
        ),
    )


def render_github_workflows():
    for nim_version in find_max_nim_versions(fetch_nim_versions()):
        render_github_workflow(nim_version)


def render_readme():
    releases = [
        release
        for release in github.repos.list_releases("elijahr", "nim-builds")
        if not release.draft and len(release.assets)
    ]
    releases = [
        {
            "nim_version": release.tag_name.split("--")[0].replace("nim-", ""),
            "date": datetime.datetime.strptime(
                release.tag_name.split("--")[1][:8], "%Y%m%d"
            ).date(),
            "page_url": f"https://github.com/elijahr/nim-builds/releases/tag/{release.tag_name}",
            "assets": [
                {"name": asset.name, "browser_download_url": asset.browser_download_url}
                for asset in sorted(release.assets, key=lambda a: a.name)
            ],
        }
        for release in releases
    ]
    releases = sorted(releases, key=lambda r: (r["nim_version"], r["date"]))
    releases = [
        list(rls)[0]
        for nim_version, rls in groupby(releases, lambda r: r["nim_version"])
    ]
    releases = sorted(
        releases, reverse=True, key=lambda r: VersionInfo.parse(r["nim_version"])
    )
    render("README.md.jinja", "README.md", dict(releases=releases))


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="subcommand")
    subparsers.add_parser("github-workflows")
    subparsers.add_parser("readme")
    args = parser.parse_args()

    if args.subcommand == "github-workflows":
        render_github_workflows()

    elif args.subcommand == "readme":
        render_readme()


if __name__ == "__main__":
    main()
