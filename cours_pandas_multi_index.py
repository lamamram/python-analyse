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

num_index = pd.Series(list(range(1, 169)) + list(range(1, 177)), name="num")
pg_multi_df = pg_df.sort_values(by="sex").set_index(["sex", num_index])

# %%
# manipulation du loc avec multi_index

pg_multi_df.loc["MALE"]
pg_multi_df.loc["MALE", 1]
# ajout des colonnes
pg_multi_df.loc[("MALE", 1), ["species", "body_mass_g"]]
# %%
# recherche fine sur un multi index
pg_multi_df.xs((2, "FEMALE"), level=["num", "sex"])
pg_multi_df.swaplevel()
# %%
# exemple complet
url = "http://raw.githubusercontent.com/BindiChen/machine-learning/main/data-analysis/031-pandas-multiIndex/dataset.csv"
data_df = pd.read_csv(
    url,
    encoding="utf8",
    # index de colonnes pour créer l'index du df
    index_col=[0, 1],
    # index de lignes pour créer les colonnes du df
    header=[0, 1]
)
data_df
# %%
# inversion des niveaux de colonnes
data_df.sort_index(axis=1, level=1).swaplevel(axis=1)

data_df["Night"]

data_df.xs("Wind", axis=1, level=1, drop_level=False)
# %%
# %%

# data_df.loc[("London", "2019-07-01"):("London", "2019-07-03"), "Day"]

# %%
