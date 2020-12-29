import json
import os
import re
import sys

from itertools import groupby
from jinja2 import Environment, StrictUndefined
from path import Path
from ruamel import yaml
from semver import VersionInfo


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
# min_version = VersionInfo.parse("1.0.10")
# min_version = VersionInfo.parse("1.2.8")


def slugify(string, delim="-", allowed_chars=""):
    return re.sub(r"[^\w%s]" % re.escape(allowed_chars), delim, string).lower()


def platform_slug(platform):
    return (
        platform.replace("linux/", "")
        .replace("arm/", "arm32")
        .replace("arm64/", "arm64")
    )


def find_max_nim_versions(versions):
    versions = (VersionInfo.parse(v.strip()) for v in versions)
    versions = (v for v in versions if v >= min_version)
    for key, versions in groupby(sorted(versions), lambda v: f"{v.major}.{v.minor}"):
        yield str(max(versions))


def fetch_nim_versions():
    return (
        v.strip()
        for v in os.popen(
            "git ls-remote --tags --refs https://github.com/nim-lang/Nim "
            "| grep -o 'refs/tags/.*' "
            "| cut -d/ -f3- | sed 's/^v//'"
        )
        .read()
        .split("\n")
        if v
    )


arch_prefix = {
    "linux/amd64": "x86_64",
    "linux/386": "i686",
    "linux/arm/v5": "armv5",
    "linux/arm/v6": "armv6",
    "linux/arm/v7": "armv7",
    "linux/arm64/v8": "aarch64",
    "linux/ppc64le": "powerpc64le",
}

arch_suffix = {
    "linux/arm/v5": "eabi",
    "linux/arm/v6": "eabihf",
    "linux/arm/v7": "eabihf",
}


def machine(distro, platform):
    return (
        f'{arch_prefix[platform]}-linux-{distro["libc"]}{arch_suffix.get(platform, "")}'
    )


def asset_id(nim_version, distro, platform):
    return f"{nim_version}--{machine(distro, platform)}"


distros = [
    {
        "name": "alpine-3-12",
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
            "debian:buster": {
                "linux/amd64": "linux/amd64",
                "linux/386": "linux/386",
                "linux/arm/v5": "linux/arm/v5",
                "linux/arm/v7": "linux/arm/v7",
                "linux/arm64/v8": "linux/arm64/v8",
                "linux/ppc64le": "linux/ppc64le",
            },
            "archlinux": {
                "linux/amd64": "linux/amd64",
                "linux/arm/v5": "linux/arm/v5",
                "linux/arm/v6": "linux/arm/v6",
                "linux/arm/v7": "linux/arm/v7",
                "linux/arm64/v8": "linux/arm64/v8",
            },
            "abyo/manjaro_aarch64": {
                "linux/arm64/v8": "linux/arm64",
            },
            "jonathonf/manjaro": {
                "linux/amd64": "linux/amd64",
            },
            "debian:buster": {
                "linux/amd64": "linux/amd64",
            },
            "ubuntu:bionic": {
                "linux/amd64": "linux/amd64",
            },
            "ubuntu:focal": {
                "linux/amd64": "linux/amd64",
            },
        },
    },
]


def render_github_workflow():
    env = Environment(autoescape=False, undefined=StrictUndefined)
    env.filters["slugify"] = slugify
    env.filters["platform_slug"] = platform_slug
    with project_dir:
        context = dict(
            distros=distros,
            nim_versions=list(find_max_nim_versions(fetch_nim_versions())),
            slugify=slugify,
            asset_id=asset_id,
        )
        build_yml = ".github/workflows/build.yml"
        with open(f"{build_yml}.jinja", "r") as f:
            rendered = env.from_string(f.read()).render(**context)
        with open(build_yml, "w") as f:
            f.write(rendered)
        print(
            "Rendered .github/workflows/build.yml.jinja -> .github/workflows/build.yml"
        )
        interpolate_yaml(build_yml)


if __name__ == "__main__":
    render_github_workflow()
