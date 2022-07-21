from conf import *
import numpy as np
import pandas as pd

def load_dns(*usecols, nrows=None):
    return pd.read_csv(
        f"{PROJECT_DIR}/dns.zip",
        encoding="iso-8859-1",
        nrows=nrows,
        usecols=usecols
    )