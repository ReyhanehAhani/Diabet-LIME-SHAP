# Published Papermill runs (actually executed)

| File | Description |
|------|-------------|
| `diabet_xai_snapshot_executed.ipynb` | Full execution with **SHAP** summary plot (parameters from `params/example.yaml`). |
| `diabet_xai_snapshot_executed.html` | Browser-friendly HTML export of the same run. |

## Reproduce locally

```bash
pip install -r papermill/requirements-papermill.txt
bash papermill/run_papermill.sh
python3 -m jupyter nbconvert --to html papermill/published/diabet_xai_snapshot_executed.ipynb --output-dir papermill/published --no-input
```
