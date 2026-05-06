#!/usr/bin/env python3
"""Baselines + evaluation + residual + permutation importance (regression)."""
from __future__ import annotations

import json
import os
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.ensemble import RandomForestRegressor
from sklearn.inspection import permutation_importance
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "modeling" / "artifacts"


def main() -> int:
    ART.mkdir(parents=True, exist_ok=True)
    bunch = load_diabetes()
    X = pd.DataFrame(bunch.data, columns=bunch.feature_names)
    y = bunch.target
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.28, random_state=42
    )
    models = {
        "ols_scaled": Pipeline(
            [("scaler", StandardScaler()), ("lr", LinearRegression())]
        ),
        "ridge": Pipeline(
            [("scaler", StandardScaler()), ("lr", Ridge(alpha=3.0))]
        ),
        "rf": RandomForestRegressor(
            n_estimators=200, max_depth=8, random_state=42, n_jobs=-1
        ),
    }
    metrics = {}
    best_name = "rf"
    best = None
    pred_best = None
    for name, est in models.items():
        est.fit(X_train, y_train)
        pred = est.predict(X_test)
        metrics[name] = {
            "mae": float(mean_absolute_error(y_test, pred)),
            "r2": float(r2_score(y_test, pred)),
        }
        if name == best_name:
            best = est
            pred_best = pred
    (ART / "metrics.json").write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    fig, ax = plt.subplots(figsize=(4.2, 4.2))
    ax.scatter(y_test, pred_best, alpha=0.35, s=12)
    lims = [min(y_test.min(), pred_best.min()), max(y_test.max(), pred_best.max())]
    ax.plot(lims, lims, "r--", lw=1)
    ax.set_xlabel("Actual")
    ax.set_ylabel("Predicted")
    ax.set_title(f"Residual check ({best_name})")
    fig.tight_layout()
    fig.savefig(ART / "pred_vs_actual.png", dpi=120)
    plt.close()
    yt = np.asarray(y_test)
    res = yt - pred_best
    fig2, ax2 = plt.subplots(figsize=(4.5, 3))
    ax2.hist(res, bins=22, color="#2b7fd4", edgecolor="white")
    ax2.set_title("Residual distribution")
    fig2.tight_layout()
    fig2.savefig(ART / "residual_hist.png", dpi=120)
    plt.close()
    result = permutation_importance(
        best, X_test, y_test, n_repeats=10, random_state=42, n_jobs=-1
    )
    order = np.argsort(result.importances_mean)[::-1][:10]
    fig3, ax3 = plt.subplots(figsize=(5, 3.5))
    ax3.barh(
        np.array(X.columns)[order][::-1],
        result.importances_mean[order][::-1],
        color="#2b7fd4",
    )
    ax3.set_xlabel("Mean R² drop")
    fig3.tight_layout()
    fig3.savefig(ART / "permutation_importance.png", dpi=120)
    plt.close()
    err = X_test.copy()
    err["y_true"] = yt
    err["y_pred"] = pred_best
    err["error"] = err["y_true"] - err["y_pred"]
    err.reindex(err["error"].abs().sort_values(ascending=False).index).head(120).to_csv(
        ART / "worst_predictions.csv", index=False
    )
    print("Wrote", ART)
    return 0


if __name__ == "__main__":
    if os.environ.get("MPLBACKEND") is None:
        os.environ["MPLBACKEND"] = "Agg"
    raise SystemExit(main())
