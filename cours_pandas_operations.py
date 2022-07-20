# %%
import os
import pandas as pd
from time import time
import numpy as np

print(pd.__version__)
print(np.__version__)

# instanciation correcte d'un rng
rng = np.random.default_rng(int(time()))
# %%

url = "http://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"
pg_df = pd.read_csv(
    url,
    encoding="utf8"
)
pg_df

# %%
# utilisation de apply sur un dataframe
def percent(s: pd.Series):
    return np.around(100 * s/s.sum(), 2)

def avg_top_n(n):
    def func(s: pd.Series):
        return s.sort_values(ascending=False)[:n].mean()
    func.__name__ = f"avg_top_{n}"
    return func

float_df = pg_df.select_dtypes("float64")
# apply applique une fonction sur toutes les colonnes
float_df.apply(percent)
# apply peut appliquer des aggrégats
float_df.apply(avg_top_n(5))
# apply peut travailler sur plusieurs colonnes sur l'axe 1
float_df["volume_mm3"] = float_df.apply(
    lambda row: 1/3 * np.pi * (row["bill_depth_mm"]/2)**2 * row["bill_length_mm"],
    axis=1
)

float_df["volume_mm3"]
# %%
# transform applique une fonction sur toutes les colonnes
float_df.transform(percent)
# transform ne peut pas appliquer d'aggrégats ni faire du multicolonnes
#transform peut appliquer plusieurs transformatons à plusieurs colonnes
float_df.transform([percent, lambda s: s / 1000])
float_df.transform({
    "body_mass_g": percent,
    "bill_length_mm": [percent, lambda s: s/1000]
})

# %%
# group by: comme en SQL
gb = pg_df[["species", "sex", "body_mass_g"]].groupby(["species", "sex"])
# l'objet gb n'est pas un df
# print(gb)
gb.mean()
# %%

# segementation
# catégories de poids: 
# 1. déterminer les valeurs de poids qui découpent
# l'ensemble des données en 3 intervalles de longueurs égales
w_min, w_max = pg_df["body_mass_g"].agg(["min", "max"])
# print(w_min, w_max)
w_cat = np.linspace(w_min, w_max, 4)
w_cat
w_labels = ["light", "medium", "heavy"]

# création de la colonne
pg_df["weight_categories"] = pd.cut(
    pg_df["body_mass_g"],
    bins=w_cat,
    labels=w_labels,
    right=False
)
pg_df[["body_mass_g", "weight_categories"]]

# nb. de pingoins par catégorie de poids
nb_pg = pg_df.shape[0]
gb = pg_df[["weight_categories", "body_mass_g"]].groupby("weight_categories")
gb["body_mass_g"].apply(lambda s: s.count()/nb_pg * 100)
# %%
# répartition statistique
pg_df["weight_categories"] = pd.qcut(
    pg_df["body_mass_g"],
    q=3,
    # labels=w_labels
)
gb = pg_df[["weight_categories", "body_mass_g"]].groupby("weight_categories")
gb["body_mass_g"].apply(lambda s: s.count()/nb_pg * 100)
# %%
