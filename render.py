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
# min_version = VersionInfo.parse("1.0.10")
# min_version = VersionInfo.parse("1.2.8")


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

toolchain_arch_to_docker_arch = {v: k for k, v in arch_prefix.items()}

toolchain_arch_aliases = {
    "x86_64": "amd64",
    "i686": "i386/i586",
    "armv5": "armel",
    "armv6": "armhf",
    "armv7": "armhf",
    "aarch64": "arm64",
    "powerpc64le": "ppc64le",
}


def asset_blurb(asset):
    toolchain = asset["name"].split("--")[1]
    arch, _, libc = toolchain.split("-")
    if libc.startswith("gnu"):
        libc_name = "GNU"
        libc_distros = "Debian, Ubuntu, Arch Linux, and Manjaro"
    elif libc.startswith("musl"):
        libc_name = "musl"
        libc_distros = "Alpine Linux"
    else:
        raise ValueError(f"Unknown libc {libc}")

    blurb = f"This was compiled for the `{arch}` aka "
    blurb += f"`{toolchain_arch_aliases[arch]}` architecture, "
    blurb += f"for distros using the {libc_name} implementation of "
    blurb += f"the C standard library, such as {libc_distros}. "
    blurb += "It can be used with Docker images targeting the "
    blurb += f"`{toolchain_arch_to_docker_arch[arch]}` platform."
    return blurb


def machine(distro, platform):
    return (
        f'{arch_prefix[platform]}-linux-{distro["libc"]}{arch_suffix.get(platform, "")}'
    )


def asset_id(nim_version, distro, platform):
    return slugify(asset_name(nim_version, distro, platform))


def asset_name(nim_version, distro, platform):
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


env = Environment(autoescape=False, undefined=StrictUndefined)
env.filters["slugify"] = slugify
env.filters["asset_blurb"] = asset_blurb


def render(path, context):
    with project_dir:
        with open(f"{path}.jinja", "r") as f:
            rendered = env.from_string(f.read()).render(**context)
        with open(path, "w") as f:
            f.write(rendered)
        print(f"Rendered {path}.jinja -> {path}")
        if path.endswith(".yml"):
            interpolate_yaml(path)


def render_github_workflow():
    render(
        ".github/workflows/build.yml",
        dict(
            distros=distros,
            nim_versions=list(find_max_nim_versions(fetch_nim_versions())),
            slugify=slugify,
            asset_id=asset_id,
            asset_name=asset_name,
        ),
    )


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
    render("README.md", dict(releases=releases))


if __name__ == "__main__":
    render_github_workflow()
    render_readme()
