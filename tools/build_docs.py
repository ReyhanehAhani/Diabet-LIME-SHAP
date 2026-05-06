#!/usr/bin/env python3
from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"


def main() -> None:
    DOCS.mkdir(parents=True, exist_ok=True)
    snap = ROOT / "papermill" / "published" / "diabet_xai_snapshot_executed.html"
    if snap.exists():
        shutil.copy(snap, DOCS / "papermill_snapshot.html")
    (DOCS / "index.html").write_text(
        """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"/>
<title>Diabet — Data lab</title>
<style>body{font-family:system-ui,sans-serif;max-width:560px;margin:3rem auto;padding:0 1rem}
a{display:block;margin:.75rem 0;color:#2b7fd4;font-weight:600}</style></head><body>
<h1>Diabetes interpretability lab</h1>
<a href="report.html">Regression baselines + residuals + permutation importance</a>
<a href="papermill_snapshot.html">Papermill SHAP snapshot</a>
</body></html>""",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
