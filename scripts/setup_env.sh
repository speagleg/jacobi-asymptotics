#!/usr/bin/env bash
# Project venv on top of the system scientific stack. Adds ONLY python-flint (spec §10).
set -euo pipefail
cd "$(dirname "$0")/.."
python3 -m venv --system-site-packages .venv
.venv/bin/pip install --no-deps -e .
.venv/bin/pip install python-flint==0.9.0
make -C csrc
# Optional: reuse a local Mathlib package cache for the Lean build if one exists (otherwise `lake` fetches it).
if [ -d /root/.cache/math-pursuits-lake/packages ]; then
  mkdir -p lean/.lake && ln -sfn /root/.cache/math-pursuits-lake/packages lean/.lake/packages
fi
.venv/bin/python -c "import jacobi_asym, flint; print('ok', jacobi_asym.__version__, flint.__version__)"
