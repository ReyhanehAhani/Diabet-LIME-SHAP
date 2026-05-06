#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MD = ROOT / "analytics" / "reports" / "case_study.md"
OUT = ROOT / "analytics" / "reports" / "DS_REPORT.html"
DOCS = ROOT / "docs" / "report.html"


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def simple_md(md: str) -> str:
    parts = []
    for block in md.split("\n\n"):
        b = block.strip()
        if not b:
            continue
        if b.startswith("# "):
            parts.append(f"<h1>{esc(b[2:])}</h1>")
        elif b.startswith("## "):
            parts.append(f"<h2>{esc(b[3:])}</h2>")
        elif b.startswith("```"):
            parts.append(f"<pre>{esc(block)}</pre>")
        else:
            if all(line.startswith("- ") for line in b.split("\n") if line.strip()):
                li = "".join(f"<li>{esc(l[2:])}</li>" for l in b.split("\n") if l.strip())
                parts.append("<ul>" + li + "</ul>")
            else:
                parts.append("<p>" + esc(b).replace("\n", "<br/>") + "</p>")
    return "\n".join(parts)


def main() -> None:
    body = simple_md(MD.read_text(encoding="utf-8"))
    art = ROOT / "modeling" / "artifacts"
    gallery = ""
    if art.exists():
        gallery = "<h2>Artifacts</h2><ul>"
        for name in ("metrics.json", "pred_vs_actual.png", "residual_hist.png", "permutation_importance.png", "worst_predictions.csv"):
            if (art / name).exists():
                gallery += f"<li><a href=\"../modeling/artifacts/{name}\">{esc(name)}</a></li>"
        gallery += "</ul>"
    html = f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"/>
<title>Diabetes DS report</title>
<style>
body{{font-family:system-ui,sans-serif;max-width:780px;margin:2rem auto;padding:0 1rem;line-height:1.55}}
pre{{background:#f5f9fc;padding:1rem;border-radius:8px;overflow:auto;font-size:0.82rem}}
a{{color:#2b7fd4}}
</style></head><body>
<p><a href="index.html">← Hub</a> · <a href="papermill_snapshot.html">SHAP snapshot (Papermill)</a></p>
{body}{gallery}
</body></html>"""
    OUT.write_text(html, encoding="utf-8")
    DOCS.parent.mkdir(parents=True, exist_ok=True)
    DOCS.write_text(html, encoding="utf-8")


if __name__ == "__main__":
    main()
