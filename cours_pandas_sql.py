# %%
import os
import sqlite3
import pandas as pd
from time import time
import numpy as np

# pip install SQLAlchemy
# créer une connexion de bdd
from sqlalchemy import create_engine
# pour créer / modifier un schéma de db
from sqlalchemy.types import Integer, String, Text

print(pd.__version__)
print(np.__version__)
# %%
# création de la base de données
try:
    # connexion db
    with sqlite3.connect("dns.db") as conn:
        # création d'un prompt pout exécuter les requêtes
        cur = conn.cursor()
        with open("domain_name_sqlite3.sql", encoding="utf8") as f:
            script = f.read()
            cur.executescript(script)
except (sqlite3.OperationalError, sqlite3.DatabaseError) as e:
    print(e)
except ConnectionError as ce:
    print(ce)

# %%
# création d'une connexion sqlite3 compatible pandas (via sqlAlchemy)

df_conn = create_engine("sqlite:///dns.db")
pays_df = pd.read_sql("pays", df_conn, index_col="iso2")
pays_df = pd.read_sql("SELECT * FROM pays WHERE name LIKE 'F%'", df_conn, index_col="iso2")
pays_df
# %%
# insertion d'un csv dans une table en passant par pandas
url = "http://www.afnic.fr/wp-media/ftp/documentsOpenData/202105_OPENDATA_A-NomsDeDomaineEnPointFr.zip"

## télécharger les données
# 1. se donner un dataframe avec l'url
# 2. écrire le df en local dans un .zip
# 3. ne faire ceci que si ce n'est pas déjà fait


## insérer les données du df dans la table domain_name
# 4. mettre en cohérence les noms des colonnes utiles
# 5. écrire le to_csv sans modifier le schéma de la table
# 6. écrire le to_csv de façon à créer (ou écraser) le schéma à partir du df