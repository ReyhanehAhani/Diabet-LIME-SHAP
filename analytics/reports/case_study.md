# Diabet project — analyst + modeling snapshot

## Data quality

`analytics/quality/validate_sklearn_diabetes.py` sanity-checks the built-in UCI-style diabetes bundle.

## Modeling

`modeling/baseline_compare.py` compares **OLS + scaling**, **Ridge**, and **RandomForest** regressors with:

- MAE / R² on holdout  
- Prediction vs actual plot  
- Residual histogram  
- Permutation importance + **worst-predictions** slice for manual error analysis  

Artifacts land in `modeling/artifacts/`.

## Papermill + HTML

The deeper **SHAP** story remains in `papermill/published/*.html`.

Run:

```bash
pip install -r requirements-analytics-stack.txt
python analytics/quality/validate_sklearn_diabetes.py
python modeling/baseline_compare.py
```
