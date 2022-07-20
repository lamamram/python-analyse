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
        with open("domain_name_sqlite3.sql") as f:
            script = f.read()
            cur.executescript(script)
except (sqlite3.OperationalError, sqlite3.DatabaseError) as e:
    print(e)
except ConnectionError as ce:
    print(ce)

# %%
