# %%
from time import time
import numpy as np
print(np.__version__)

# instanciaiton correcte d'un rng
rng = np.random.default_rng(int(time()))
# %%
import sys

# une range est un générateur (génère les données à la demande)
r = range(1000)
lst = list(r)
arr = np.array(r)
print(sys.getsizeof(r), sys.getsizeof(lst), sys.getsizeof(arr))
# arr
# %%
# manipulation des types
arr = arr.astype("i2")
arr = arr.astype(np.int64)
np.array([1, 2, 3], dtype="i1")
print(sys.getsizeof(arr))
# %%
# filtrage
values = rng.integers(0, 100, size=20)
sup_5 = values > 5
values[ values > 5 ]

# %%
# exercice de filtres numpy:
# à partir de deux tableaux numpy d'entiers générés aléatoirement
# donner le tableau des éléments non communs aux deux tableaux
from numpy.ma import masked_array

arr1, arr2 = [ rng.integers(1, 100, endpoint=True, size=20, dtype=np.int8) for _ in range(2) ]
print(f"arr1 = {arr1}")
print(f"arr2 = {arr2}")

# HINT: np.union1d, np.intersect1d, np.isin

union = np.union1d(arr1, arr2)
inter = np.intersect1d(arr1, arr2)
cond = ~np.isin(union, inter)

# valeurs
print(union[ cond ])

# idem avec masked_array
masked= masked_array(union, mask=np.isin(union, inter))
print(masked)
print(masked[masked.mask == False])

# indices des True
np.where(cond)
# tableau masqué
# %%
# données manquantes

data = np.array([1., 4.32, 3.14, 4, "N/A", "INF", None])
print(data.dtype)
# substitutions
data[ data == "N/A"] = np.nan
data[ data == "INF"] = np.inf

data = data.astype(float)
# nan et inf sont englobants
data.mean()
clean_inf = data[~np.isinf(data)]
clean_nan = clean_inf[~np.isnan(clean_inf)]
# isnan inclue None : pas de np.isnull()
clean_nan.mean()
# %%
