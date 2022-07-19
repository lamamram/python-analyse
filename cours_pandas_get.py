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
# pb avec jupyter
# PROJECT_DIR = os.path.dirname(__file__)
PROJECT_DIR = os.path.abspath("")
df = pd.read_csv(
    f"{PROJECT_DIR}/users.csv",
    delimiter=";",
    encoding="utf8",
    index_col=0,
    na_values=["--"],
    # usecols est traité avant index_col
    usecols=["Unnamed: 0", "name", "age", "size"]
)
df
# %%
# introspection
df.head()
df.tail()
df.shape
df.describe()
df.dtypes
# %%
# nettoyage d'une valeur de mauvais type
# version 1
df_alt = df.copy()
df_alt["age"]
# type(df_alt["age"])
df_alt["age"] = df_alt["age"].apply(
    lambda elem: elem if elem.isnumeric() else np.nan)
# virer les nan
clean_age = df_alt["age"].dropna()
clean_age.astype("int8")
# convertir les nan
# mettre à jour un df_alt ou une série
# 1. réaffectation df_alt = df_alt.xxxx => DataFrame ou Series
# 2. utilisation du param df_alt.xxxx(inplace=True) => None
df_alt["age"].fillna(0, inplace=True)
df_alt = df_alt.astype({
    "age": "int8"
})
df_alt
# %%
df_alt2 = df.copy()
# version 2: travailler dirctement sur l'objet series
# grâce à l'attribut str qui propose des versions vectorisées
# des fonctions usuelles de la classe builtin str
df_alt2["age"].str.extract("^(\d+)$")
# %%
# appel d'une colonne
df["age"]
df.age
# %%
# appel de plusieurs colonnes
df[ ["age", "name"] ]
# slicing sur les noms de colonnes
df["name":]
# %%
# slicing sur les lignes (fin non comprise)
df[0:2]
# slicing sur les valeurs d'index (fin compris)
df["user1":"user3"]
# %%
# filtrage de ligne par valeurs de colonnes
df_alt[ df_alt.age > 40 ]
# %%
# sélection lignes / colonnes
df_alt.loc["user1":"user2", ["name", "size"]]
df_alt.loc[df_alt.age > 40, ["name", "size"]]

df_alt.iloc[0:2, 0:2]

df_alt.at["user2", "name"]
df_alt.iat[1,1]
# %%
