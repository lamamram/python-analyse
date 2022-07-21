import numpy as np
import pandas as pd

def percent(s: pd.Series):
    return np.around(100 * s/s.sum(), 2)