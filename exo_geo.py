# %%
from conf import *
import pandas as pd
import numpy as np
from time_context import TimerCtx
from utils import load_dns
# %%
# 1. écrire une fonction qui ouvre le fichier dns.zip avec certaines colonnes

# 2. avec cette fction, créer un df avec uniquement les colonnes Pays BE et Ville BE
cols = ["Pays BE", "Ville BE"]
dns_df = load_dns("Pays BE", "Ville BE", nrows=1000000)
dns_df = load_dns(*cols, nrows=1000000)
dns_df

# 3. transformer le df pour obtenir 3 colonnes
# pays, ville et nombre de dns par ville
# Hint: regarder la fonction value_counts des dataframes
s = dns_df.groupby(["Pays BE", "Ville BE"]).value_counts()
s.name = "nb"
dns_df = s.reset_index()
dns_df
# %%
# 4. ouvrir le df geo_dns et nettoyer la colonne loc pour la mettre
# en cohérence avec la colonne Ville BE
# Hint: utiliser les fonction .str.replace et .str.split des séries de type object
geo_df = pd.read_csv(
    "geo_dns.csv",
    encoding="utf8",
    index_col=0
)
geo_df["loc"] = geo_df["loc"].str.replace(
    ", ([A-Z]{2})$",
    repl=lambda m: "|" + m.group(1),
    regex=True
)
geo_df[["loc", "iso2"]] = geo_df["loc"].str.split("|", expand=True)
geo_df

# 5. joindre les deux dataframes pour obtenir 5 colonnes avec lat, lon
pd.merge(
    dns_df, geo_df,
    how="inner",
    left_on=["Pays BE", "Ville BE"],
    right_on=["iso2", "loc"]).drop(columns=["iso2", "loc"])

# 6. afficher les marqueurs sur une carte folium
# %%
