# %%
import os
import pandas as pd
from time import time
import numpy as np

print(pd.__version__)
print(np.__version__)

# instanciation correcte d'un rng
rng = np.random.default_rng(int(time()))
# %%

# fabrication du df:
# 1. une colonne student avec 10 valeurs répétées 4 fois
# 2. une colonne subject avec 4 valeurs répétées dans l'ordre 10 fois
# 3. une colonne note avec des entiers entre 0 et 20 (avec les 0.5 possibles)
# 4. une colonne coeff qui répètent les mêmes valeurs en focntion du subject

students = ["student_{i}" for i in range(1, 11)]
subjects = ["math", "english", "biology", "history"]
coeffs = [3, 2, 2, 1]

note_df = pd.DataFrame({
    "student": [],
    "subject": [],
    "note": [],
    "coeff": []  
})