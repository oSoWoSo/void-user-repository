#!/usr/bin/env python3
"""Remove package entries from an xbps repodata file.

The repodata file is a (possibly gzip-compressed) tar archive containing
`index.plist` and optionally `index-files.plist` and `index-meta.plist`,
all in Apple XML plist format with package names as top-level keys.

Usage:
    repodata-strip.py REPODATA NAME [NAME...]

Exit status 0 on success (including no-op when no listed name was present),
nonzero on parse or I/O failure.
"""

from __future__ import annotations

import io
import os
import plistlib
import sys
import tarfile

INDEX_FILES = {"index.plist", "index-files.plist"}


def open_tar_any(path: str) -> tarfile.TarFile:
    """Open a tar that may be plain, gzip, or bzip2. xbps uses plain tar,
    but tolerate older variants in case the server has one of those.
    """
    with open(path, "rb") as f:
        magic = f.read(6)
    if magic[:2] == b"\x1f\x8b":
        return tarfile.open(path, mode="r:gz")
    if magic[:3] == b"BZh":
        return tarfile.open(path, mode="r:bz2")
    if magic[:4] == b"\x28\xb5\x2f\xfd":
        sys.stderr.write(
            "error: zstd-compressed repodata is not supported by this tool\n"
        )
        sys.exit(2)
    return tarfile.open(path, mode="r:")


def main() -> int:
    if len(sys.argv) < 2:
        sys.stderr.write(f"Usage: {sys.argv[0]} REPODATA [NAME...]\n")
        return 2
    repodata = sys.argv[1]
    drop = set(sys.argv[2:])
    if not drop:
        return 0
    if not os.path.isfile(repodata):
        sys.stderr.write(f"error: not a file: {repodata}\n")
        return 1

    # Detect compression mode for round-trip write
    with open(repodata, "rb") as f:
        magic = f.read(2)
    write_mode = "w:gz" if magic == b"\x1f\x8b" else "w:"

    members: list[tuple[tarfile.TarInfo, bytes]] = []
    with open_tar_any(repodata) as tf:
        for m in tf.getmembers():
            extracted = tf.extractfile(m)
            data = extracted.read() if extracted is not None else b""
            members.append((m, data))

    total_removed = 0
    rewritten: list[tuple[tarfile.TarInfo, bytes]] = []
    for m, data in members:
        if m.name in INDEX_FILES and m.isfile():
            try:
                idx = plistlib.loads(data)
            except Exception as e:
                sys.stderr.write(f"error: failed to parse {m.name}: {e}\n")
                return 1
            if not isinstance(idx, dict):
                rewritten.append((m, data))
                continue
            removed = [k for k in list(idx) if k in drop]
            for k in removed:
                del idx[k]
            if removed:
                total_removed += len(removed)
                print(
                    f"  {m.name}: removed {len(removed)} entries "
                    f"({', '.join(removed)})"
                )
                data = plistlib.dumps(idx, fmt=plistlib.FMT_XML)
                m.size = len(data)
        rewritten.append((m, data))

    if total_removed == 0:
        print("  no matching entries in repodata; nothing to do")
        return 0

    tmp = repodata + ".tmp"
    try:
        with tarfile.open(tmp, mode=write_mode) as tf:
            for m, data in rewritten:
                tf.addfile(m, io.BytesIO(data))
        os.replace(tmp, repodata)
    except Exception:
        if os.path.exists(tmp):
            os.unlink(tmp)
        raise
    return 0


if __name__ == "__main__":
    sys.exit(main())
