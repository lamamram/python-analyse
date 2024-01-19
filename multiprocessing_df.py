# %% [markdown]
# ### calcul multiprocessing
# 
# #### énoncé
# 1. avaler le fichier villes_france.zip dans pandas
# 2. transformer le zipcode en département
# 3. créer un "worker" qui calcule la combinaison de toutes les distances de villes dans un dpt
# 4. multiprocesser les worker dans la pool
# 5. réduire le max total des max locaux

# %%
import os, sys
from re import sub
import pandas as pd
import numpy as np
from latloncalc.latlon import LatLon, Latitude, Longitude
from itertools import combinations
from multiprocessing import Pool, cpu_count, current_process
from decorators import timer

# %%
villes_df = pd.read_csv(
    "villes_france.zip",
    encoding="utf8",
    # il n'y a pas d'header
    header=None,
    # donner des nom des colonnes
    names=["city", "zipcode", "lon", "lat"]
)
villes_df

# %%
# transformation du zipcode en dept 
def get_dept(zc: str):
    return "0" + zc[0] if len(zc) < 5 else zc[:2]

villes_df["zipcode"] = villes_df["zipcode"].apply(get_dept)
villes_df.rename(columns={"zipcode": "dept"}, inplace=True)
villes_df

# %%
# trouver des doublons de villes + dept
villes_df.drop_duplicates(subset=["city", "dept"], keep="first", inplace=True)

# %%
# cas de test
# creuse_df = villes_df.loc[ villes_df["dept"] == "23" ].set_index("city")
# calcule des distances des combinaisons à 2 des villes d'un département
# en trouvant le max
def max_geodesic(df: pd.DataFrame):
    max_d, itinerary = 0, ""
    for v1, v2 in combinations(df.index, r=2):
        point1 = LatLon(Latitude(df.loc[v1]["lat"]), Longitude(df.loc[v1]["lon"]))
        point2 = LatLon(Latitude(df.loc[v2]["lat"]), Longitude(df.loc[v2]["lon"]))
        d = point1.distance(point2)
        if d > max_d:
            max_d = d
            itinerary = f"{v1} <-> {v2}" 
    return  itinerary, max_d
        
# cas d'un département
# max_geodesic(creuse_df)
  

# %%
# cas unique
# point1 = LatLon(Latitude(creuse_df.loc["VIERSAT"]["lat"]), Longitude(creuse_df.loc["VIERSAT"]["lon"]))
# point2 = LatLon(Latitude(creuse_df.loc["LUSSAT"]["lat"]), Longitude(creuse_df.loc["LUSSAT"]["lon"]))
# d = point1.distance(point2)
# d

# %%
@timer
def process():
    depts = ["23", "13"] #, "33", "44", "15" "29" "78", "81", "50"]
    villes_df.set_index("city", inplace=True)
    with Pool(cpu_count() - 2) as pool:
        ## pool apply => application d'un worker sur un cpu de la pool de manière synchrone
        ## pool apply_async =>  //                 //           //       //       asynchronique
        # il faut requêter sur le retour de type AsyncResult via o.get()
        # pour être sûr il faut attendre le pool.join() qui va bloquer le programme jusqu'à la fin des 
        # workers
        ## pool map => application d'une grappe de worker (même finction) de la manière synchrone
        # donne la liste de retour des workers
        # WARNING: le worker n'a qu'un seul paramètre
        # pour plusieurs paramètres pool.starmap(fn, [(),(),()])
        ## pool map_async idem non bloquant => pool.join()
        params = [ villes_df.loc[ villes_df["dept"] == dpt ] for dpt in depts ]
        results = pool.map(
            max_geodesic,
            params            
        )
        results = dict(zip(depts, results))
        print(results)
        results = sorted(results.items(), key=lambda r: r[1][1], reverse=True)
        print(results[0])

if __name__ == "__main__":
    process()

# %%



