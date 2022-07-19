import numpy as np
import pandas as pd

def percent(s: pd.Series):
    return np.around(100 * s/s.sum(), 2)

def percent_agg(s: pd.Series):
    return np.around(100 * s.sum()/s.count(), 2)

def avg_top_n(n):
    def func(s: pd.Series):
        return s.sort_values(ascending=False)[:n].mean()
    func.__name__ = f"avg_top_{n}"
    return func