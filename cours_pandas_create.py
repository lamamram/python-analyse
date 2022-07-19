# %%
import pandas as pd
from time import time
import numpy as np
print(pd.__version__)
print(np.__version__)

# instanciaiton correcte d'un rng
rng = np.random.default_rng(int(time()))

# %%
# instanciation canonique


data = [
    ["jimmy", 28, "2 rue de la rép, 44000 NANTES", 1.73],
    ["Joan", 33, "12 bd Haussmann 75009 Paris", 1.56],
    # ["Joan", 33, "12 bd Haussmann 75009 Paris"],
    ["Paul", 76, "10, chemin des lilas, 13002 MaRSEILLE", 1.85],
]
columns = ["name", "age", "address", "size"]
index = ["user1", "user2", "user3"]
df = pd.DataFrame(
    data=data,
    columns=columns,
    index=index
)
# panda comble les données incomplètes avec NaN
df
# %%
# instanciations à partir d'une liste des séries stat
mtrx = np.array(data)
series = mtrx.transpose()
series = dict(zip(columns, series))
series
df = pd.DataFrame(data=series, index=index)
df


# %%
# données sous forme de listes d'objets json (réponse REST)
records = np.apply_along_axis(
    lambda row: dict(zip(columns, row)),
    axis=1,
    arr=data
)
# del records[1]["size"]
df = pd.DataFrame.from_records(records, index=index)
df
# %%

# écriture dans un csv
df.to_csv(
    "users.csv",
    sep=";",
    encoding="utf8",
    index=True 
)
# %%
df = pd.read_csv(
    "users.csv",
    delimiter=";",
    index_col=0
)
df
# %%
df.to_json("users.json",
            orient="records",
            # gestion des caractères non ascii
            force_ascii=False
            # orient="index"
            # orient="table"
)
# %%
