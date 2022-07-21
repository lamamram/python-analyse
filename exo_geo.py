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


# 4. ouvrir le df geo_dns et nettoyer la colonne loc pour la mettre
# en cohérence avec la colonne Ville BE
# Hint: utiliser les fonction .str.replace et .str.split des séries de type object

# 5. joindre les deux dataframes pour obtenir 5 colonnes avec lat, lon

# 6. afficher les marqueurs sur une carte folium
# %%
