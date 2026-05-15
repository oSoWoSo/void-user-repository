#!/usr/bin/env python3
"""List package names from an xbps repodata index.

Reads the `index.plist` member of an xbps repodata tar archive and prints
each top-level key (= package name as published) on its own line.

Usage:
    repodata-list.py REPODATA

Exit status 0 on success (output may be empty if the index is empty),
2 on usage/format errors, 1 on I/O or parse failure.
"""

from __future__ import annotations

import plistlib
import sys
import tarfile


def open_tar_any(path: str) -> tarfile.TarFile:
    with open(path, "rb") as f:
        magic = f.read(4)
    if magic[:2] == b"\x1f\x8b":
        return tarfile.open(path, mode="r:gz")
    if magic[:3] == b"BZh":
        return tarfile.open(path, mode="r:bz2")
    if magic[:4] == b"\x28\xb5\x2f\xfd":
        sys.stderr.write("error: zstd-compressed repodata is not supported\n")
        sys.exit(2)
    return tarfile.open(path, mode="r:")


def main() -> int:
    if len(sys.argv) != 2:
        sys.stderr.write(f"Usage: {sys.argv[0]} REPODATA\n")
        return 2
    try:
        with open_tar_any(sys.argv[1]) as tf:
            for m in tf.getmembers():
                if m.name == "index.plist" and m.isfile():
                    f = tf.extractfile(m)
                    if f is None:
                        return 1
                    data = plistlib.loads(f.read())
                    if not isinstance(data, dict):
                        sys.stderr.write("error: index.plist is not a dict\n")
                        return 1
                    for k in data:
                        print(k)
                    return 0
    except (tarfile.TarError, OSError, plistlib.InvalidFileException) as e:
        sys.stderr.write(f"error: {e}\n")
        return 1
    sys.stderr.write("error: no index.plist in repodata\n")
    return 1


if __name__ == "__main__":
    sys.exit(main())
