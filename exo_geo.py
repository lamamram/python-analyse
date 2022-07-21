# %%
import pandas as pd
from time import time
import numpy as np
from time_context import TimerCtx

# %%
# 1. écrire une fonction qui ouvre le fichier dns.zip avec certaines colonnes
dns_df = pd.read_csv(
    "dns.zip",
    encoding="iso-8859-1",
    nrows=1000000,
    usecols=["Nom de domaine", "Pays BE", "Date de création"]
)
# 2. avec cette fction, créer un df avec uniquement les colonnes Pays BE et Ville BE

# 3. transformer le df pour obtenir 3 colonnes
# pays, ville et nombre de dns par ville
# Hint: regarder la fonction value_counts des dataframes

# 4. ouvrir le df geo_dns et nettoyer la colonne loc pour la mettre
# en cohérence avec la colonne Ville BE
# Hint: utiliser les fonciton .str.replace et .str.split des séries de type object

# 5. joindre les deux dataframes pour obtenir 5 colonnes avec lat, lon

# 6. afficher les marqueurs sur une carte folium