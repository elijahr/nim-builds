import json
import os
import re
import sys

from itertools import groupby
from semver import VersionInfo

min_version = VersionInfo.parse("1.0.10")


def find_max_nim_versions(versions):
    versions = (VersionInfo.parse(v.strip()) for v in sorted(versions))
    versions = (v for v in versions if v >= min_version)
    for key, versions in groupby(versions, lambda v: f"{v.major}.{v.minor}"):
        yield str(max(versions))

def fetch_nim_versions():
    return (
        v.strip()
        for v in
        os.popen(
            "git ls-remote --tags --refs https://github.com/nim-lang/Nim "
            "| grep -o 'refs/tags/.*' "
            "| cut -d/ -f3- | sed 's/^v//'"
        )
        .read()
        .split("\n")
        if v
    )

if __name__ == "__main__":
    versions = json.dumps(list(find_max_nim_versions(fetch_nim_versions())))
    build_yml = os.path.join(os.path.dirname(__file__), '.github/workflows/build.yml')
    with open(build_yml, 'r') as f:
        new_contents = re.sub(r'nim-version: \[.*', f'nim-version: {versions}', f.read())
    with open(build_yml, 'w') as f:
        f.write(new_contents)


