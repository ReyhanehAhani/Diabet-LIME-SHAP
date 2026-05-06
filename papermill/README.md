# Pillar 2 — Reproducibility (Papermill)

The main notebook `Diabet-LIME-SHAP.ipynb` is a full deep dive. This folder adds a **small parameterized notebook** you can re-execute with different `random_state` / sample caps for demos, ablations, or portfolio screenshots.

```bash
pip install -r papermill/requirements-papermill.txt
bash papermill/run_papermill.sh
```

Outputs land in `papermill/reports/` as timestamped executed notebooks.

## Resume

- *Used **Papermill** to freeze diabetes interpretability experiments with explicit random seeds and exportable HTML/PDF artifacts.*
