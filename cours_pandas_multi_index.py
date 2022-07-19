# %%
import os
import pandas as pd
from time import time
import numpy as np

print(pd.__version__)
print(np.__version__)

# instanciaiton correcte d'un rng
rng = np.random.default_rng(int(time()))

# %%
url = "http://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"
pg_df = pd.read_csv(
    url,
    encoding="utf8"
)
pg_df

print(pg_df.loc[pg_df.sex == "MALE", "sex"].count())
print(pg_df.loc[pg_df.sex == "FEMALE", "sex"].count())

num_index = pd.Series(list(range(1, 166)) + list(range(1, 180)), name="num")
pg_multi_df = pg_df.set_index(["sex", num_index])

# %%
# manipulation du loc avec multi_index

# %%
