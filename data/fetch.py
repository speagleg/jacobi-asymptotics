"""Fetch large data into data/raw (gitignored) and verify sha256.  Usage: python data/fetch.py odlyzko"""
import gzip
import hashlib
import shutil
import sys
import urllib.request
from pathlib import Path
import numpy as np

RAW = Path(__file__).resolve().parent / "raw"
import os
# Optional local copy (set JA_ZEROS6_LOCAL to a zeros6.gz path); otherwise the file is downloaded from URL.
LOCAL = Path(os.environ.get("JA_ZEROS6_LOCAL", "/nonexistent/zeros6.gz"))
URL = "https://www-users.cse.umn.edu/~odlyzko/zeta_tables/zeros6.gz"
SHA = {"zeros6.gz": "6acacb4707c429bf368f32823a8eef0e0737b6318d3e144c78975a4986d155da"}


def sha256(path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def odlyzko():
    RAW.mkdir(parents=True, exist_ok=True)
    gz = RAW / "zeros6.gz"
    if not gz.exists():
        if LOCAL.exists():
            shutil.copyfile(LOCAL, gz)
        else:
            urllib.request.urlretrieve(URL, gz)
    if sha256(gz) != SHA["zeros6.gz"]:
        raise SystemExit(f"sha256 mismatch for {gz}")
    with gzip.open(gz, "rt") as f:
        g = np.array([float(l) for l in f if l.strip()])
    if g.size != 2001052 or not np.all(np.diff(g) > 0):
        raise SystemExit("unexpected zeros6 content")
    np.save(RAW / "zeta_zeros_odlyzko6.npy", g)
    print("ok", g.size, sha256(RAW / "zeta_zeros_odlyzko6.npy"))


if __name__ == "__main__":
    {"odlyzko": odlyzko}[sys.argv[1]]()
