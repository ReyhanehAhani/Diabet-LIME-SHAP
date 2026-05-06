# DiabetesLIME-SHAP

## Description
This project utilizes the interpretability tools LIME (Local Interpretable Model-agnostic Explanations) and SHAP (SHapley Additive exPlanations) to explore and explain predictions made by machine learning models on diabetes data. The focus is on enhancing transparency and understanding of how input features influence model predictions, aiding in more informed decision-making in healthcare analytics.

## Installation
Ensure the following Python packages are installed to run this notebook:
- pandas
- seaborn
- matplotlib
- lime
- shap
- keras
- numpy

Install these packages via pip:
```bash
pip install pandas seaborn matplotlib lime shap keras numpy
```

## Portfolio — Pillar 2 (Papermill)

A compact `RandomForest + SHAP` notebook lives in `papermill/notebooks/diabet_xai_snapshot.ipynb`. After `pip install -r papermill/requirements-papermill.txt`, run:

```bash
bash papermill/run_papermill.sh
```

to materialize timestamped executed notebooks under `papermill/reports/` (ignored by git) for reproducible CV screenshots.

**Checked-in proof run:** `papermill/published/diabet_xai_snapshot_executed.html` (+ matching `.ipynb`) — open the HTML in any browser to see SHAP output from a parameterized run.

## Regression baselines + error analysis

```bash
pip install -r requirements-analytics-stack.txt
python analytics/quality/validate_sklearn_diabetes.py
python modeling/baseline_compare.py
python analytics/reports/build_report.py
python tools/build_docs.py
```

CI: `.github/workflows/data-stack.yml`.
