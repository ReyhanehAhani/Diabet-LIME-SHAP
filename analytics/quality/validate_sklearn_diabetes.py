#!/usr/bin/env python3
"""Schema checks on sklearn diabetes tabular matrix."""
from __future__ import annotations

import sys

import numpy as np
from sklearn.datasets import load_diabetes


def main() -> int:
    X, y = load_diabetes(return_X_y=True)
    if X.shape[1] != 10 or len(y) != X.shape[0]:
        print("unexpected diabetes shape", file=sys.stderr)
        return 1
    if np.isnan(X).any() or np.isnan(y).any():
        print("nan in built-in diabetes", file=sys.stderr)
        return 1
    print("OK: sklearn diabetes bundle passes quality checks.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
