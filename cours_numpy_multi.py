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
# redimensionnement
mtrx.reshape(6, -1)
# ValueError
# mtrx.reshape(5, -1)

# %%
# notion d'axes
patient1 = np.array([64.6, 173.8, 132, 85])
patient2 = np.array([52.4, 163.9, 149, 94])
patients = np.array([patient1, patient2])
patients

patients.mean()
# moyenne des poids, tailles tension
(patient1 + patient2) / 2
patients.mean(axis=0)

# axe1 => non signifiant
np.array([patient1.mean(), patient2.mean()])
patients.mean(axis=1).reshape(2, 1)
# %%
# fonction custom sur un axe
# ex: poids / taille**2

np.apply_along_axis(lambda r: r[0]/(r[1]/100)**2, axis=1, arr=patients)

# %%
other_patients = np.genfromtxt(
    "patients.txt",
    encoding="utf8",
    delimiter=",",
    skip_header=1,
    comments="//",
    missing_values="???",
    filling_values=0.,
    usecols=(0,1,2,3),
    # dtype="f8,f8,i4,i4,U3"
    dtype="f8"
)
other_patients.ndim
# other_patients["f0"].mean()
# %%
# %%
# ajouts des nouvelles lignes en bas
np.concatenate([patients, other_patients], axis=0)

# ajout des nouvelles lignes à droite
# np.concatenate([patients, other_patients], axis=1)
# %%
# idem avec append (on ajoute des colonnes à droite, d'où le reshape)
patients
np.append(patients, axis=0, values=[[1, 2, 3, 4]])
np.append(patients, axis=1, values=np.array([1, 2]).reshape(2, 1))
# %%
