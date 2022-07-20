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
