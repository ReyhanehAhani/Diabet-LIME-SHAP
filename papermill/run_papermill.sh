#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PARAMS="${1:-$ROOT/papermill/params/example.yaml}"
OUT_DIR="$ROOT/papermill/reports"
mkdir -p "$OUT_DIR"
STAMP="$(date +%Y%m%d_%H%M%S)"
OUT_NB="$OUT_DIR/diabet_snapshot_${STAMP}.ipynb"

papermill "$ROOT/papermill/notebooks/diabet_xai_snapshot.ipynb" "$OUT_NB" -f "$PARAMS" --log-output
echo "Wrote $OUT_NB"
