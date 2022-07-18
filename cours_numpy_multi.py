# %%
from time import time
import numpy as np
print(np.__version__)

# instanciaiton correcte d'un rng
rng = np.random.default_rng(int(time()))

# %%

mtrx = np.array([
    [1, 3, 6, 0],
    [-6, 8, 12, 5],
    [6, 3, -7, 3]
])

print(mtrx)
print(f"nb de dimension: {mtrx.ndim}")
print(f"nb lignes x nb colonnes: {mtrx.shape}")

# %%
# notion d'axes
patient1 = np.array([64.6, 173.8, 132, 85])
patient2 = np.array([52.4, 163.9, 149, 94])
patients = np.array([patient1, patient2])
patients
