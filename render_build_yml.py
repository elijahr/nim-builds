import json
import os
import re
import sys

from itertools import groupby
from jinja2 import Environment, StrictUndefined
from path import Path
from semver import VersionInfo


project_dir = Path(os.path.dirname(os.path.abspath(__file__)))
min_version = VersionInfo.parse("1.0.10")


def slugify(string, delim="-", allowed_chars=""):
    return re.sub(r"[^\w%s]" % re.escape(allowed_chars), delim, string).lower()


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


distros = [
    {
        "name": "alpine-3-12",
        "build_farm_host_image": "elijahru/build-farm:alpine-3.12",
        "build_farm_client_image": "elijahru/build-farm-client:alpine-3.12",
        "platforms": [
            "linux/amd64",
            "linux/386",
            "linux/arm/v6",
            "linux/arm/v7",
            "linux/arm64/v8",
        ],
    },
    {
        "name": "archlinux",
        "build_farm_host_image": "elijahru/build-farm:archlinux",
        "build_farm_client_image": "elijahru/build-farm-client:archlinux",
        "platforms": [
            "linux/amd64",
            "linux/arm/v5",
            "linux/arm/v6",
            "linux/arm/v7",
            "linux/arm64/v8",
        ],
    },
    {
        "name": "debian-buster",
        "build_farm_host_image": "elijahru/build-farm:debian-buster-slim",
        "build_farm_client_image": "elijahru/build-farm-client:debian-buster-slim",
        "platforms": [
            "linux/amd64",
            "linux/386",
            "linux/arm/v5",
            "linux/arm/v7",
            "linux/arm64/v8",
            "linux/ppc64le",
            "linux/s390x",
            "linux/mips64le",
        ],
    },
]


def render_build_yml():
    env = Environment(autoescape=False, undefined=StrictUndefined)
    env.filters["slugify"] = slugify
    with project_dir:
        context = dict(
            distros=distros,
            nim_versions=list(find_max_nim_versions(fetch_nim_versions())),
            slugify=slugify,
        )
        with open(project_dir / ".github/workflows/build.yml.jinja", "r") as f:
            rendered = env.from_string(f.read()).render(**context)
        with open(project_dir / ".github/workflows/build.yml", "w") as f:
            f.write(rendered)
        print(
            "Rendered .github/workflows/build.yml.jinja -> .github/workflows/build.yml"
        )


if __name__ == "__main__":
    render_build_yml()

    # versions = json.dumps(list(find_max_nim_versions(fetch_nim_versions())))
    # build_yml = os.path.join(os.path.dirname(__file__), '.github/workflows/build.yml.jinja')
    # with open(build_yml, 'r') as f:
    #     new_contents = re.sub(r'nim-version: \[.*', f'nim-version: {versions}', f.read())
    # with open(build_yml, 'w') as f:
    #     f.write(new_contents)
