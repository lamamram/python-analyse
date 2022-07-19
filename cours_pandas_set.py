# %%
import os
from pickletools import int4
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
pg_df.head(20)
# %%
# analyse de n lignes à l'offset o
def analyse_df(df, limit=10, offset=0):
    return df.iloc[offset: offset + limit]

analyse_df(pg_df, 20, 100)
# %%
# masse en kg
pg_df.body_mass_g /= 1000
pg_df.rename(columns={
    "body_mass_g": "mass_kg"
}, inplace=True)
# %%
masses = pg_df["mass_kg"]
masses.name = "m_kg"
masses

# %%
pg_df["bill_volume_mm3"] = 1/3 * np.pi * (pg_df.bill_depth_mm/2)**2 * pg_df.bill_length_mm
pg_df["bill_volume_mm3"] = np.around(pg_df["bill_volume_mm3"], 2)
pg_df

# %%
# suppression colonne
pg_df.drop(columns={
    "bill_volume_mm3"
}, inplace=True)
# %%
# ajout à l'index
s = 1/3 * np.pi * (pg_df.bill_depth_mm/2)**2 * pg_df.bill_length_mm
pg_df.insert(4, "bill_volume_mm3", s)
pg_df
# %%
# réarangement de columns
# transformation d'un index en liste pour opération mutable
cols = pg_df.columns.to_list()
rng.shuffle(cols)
pg_df = pg_df[cols]
pg_df
# %%
# tris
# axe 0 : lignes, axe 1: colonnes
pg_df.sort_index(axis=1, inplace=True)
pg_df

pg_df.sort_values(by=["sex", "body_mass_g"], ascending=[True, False], inplace=True)
pg_df
# %%
# aggrégats statistiques par défaut
pg_df.describe()
# aggrégats ciblés sur un type de données
float_df = pg_df.select_dtypes(include=["float64"])
float_df.median()
# %%
# aggrégats custom
def q33(s: pd.Series):
    return s.quantile(0.33)

# fermeture: fonction qui contrôle le contexte d'exécution d'une autre fonction
def avg_top_n(n):
    def func(s: pd.Series):
        return s.sort_values(ascending=False)[:n].mean()
    func.__name__ = f"avg_top_{n}"
    return func

pg_df.agg({
    "bill_length_mm": ["mean", np.std],
    "body_mass_g": ["min", q33, avg_top_n(5)]
})



# %%
