# %%
import os
import pandas as pd
from time import time
import numpy as np
from pyparsing import col

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

students = [f"student_{i}" for i in range(1, 11)]
subjects = ["math", "english", "biology", "history"]
coeffs = [3, 2, 2, 1]

notes = rng.integers(0, 40, endpoint=True, size=40) / 2

note_df = pd.DataFrame({
    "student": np.repeat(students, repeats=4),
    "subject": np.tile(subjects, reps=10),
    "note": notes,
    "coeff": np.tile(coeffs, reps=10),
})
note_df
# %%
# pivot: passage du format long au format large
pivoted_df = note_df.pivot(
    index="student",
    # colonne dont les valeurs vont devenir
    # les colonnes du df pivoté
    columns="subject",
    # colonnes dont les valeurs vont être 
    # dispatchées dans les nouvelles colonnes
    values=["note", "coeff"]
)
pivoted_df.sort_index(axis=1, level=1).swaplevel(axis=1)
pivoted_df

# %%
# moyenne pondérée par étudiant
pivoted_df.apply(
    lambda s: np.average(s["note"], weights=s["coeff"]),
    axis=1
)

# %%
# inversion du pivot multi-colonnes
# la méthode stack réarrange un niveau de colonne en niveau d'index
# reset_index remise un niveau d'index en tant que colonne
pivoted_df.stack(level=1).reset_index()

# %%
# inversion du pivot simples colonnes
wide_df = pivoted_df.drop(columns="coeff").droplevel(axis=1, level=0).reset_index()
# suppression du nom d'index des colonnes
wide_df.columns.name = None
wide_df
wide_df.melt(
     # conserver l'index si index
     # ignore_index=False,
     # conserver des colonnes indépendantes du pivot
     id_vars="student",
     # renommages des colonnes variable et value
     var_name="subject",
     value_name="note",
     # colonnes qui vont alimenter la colonne variable
     # par défaut, tout sauf id_vars
     # value_vars=["math", "english"]
)
# %%
# pivot_table: pivoter et calculer des aggrégats
school_df = note_df.copy()
school_df.insert(0, "school", ["public"] * 20 + ["private"] * 20)
school_df
# calcul du format large pour obtenir la moyenne par matière
pivoted_table_df =pd.pivot_table(
    school_df,
    index="school",
    columns="subject",
    values=["note", "coeff"],
    aggfunc=np.mean
    # aggfunc=(np.mean, np.max)
)
pivoted_table_df
pivoted_table_df.apply(
    lambda s: np.average(s["note"], weights=s["coeff"]),
    axis=1
)
# %%
# fonctions de répétition numpy
np.repeat([1, 2, 3, 4], repeats=10)

np.tile([1, 2, 3, 4], reps=10)
# %%
students_df = pd.DataFrame({
    "scholar": [f"student_{i}" for i in range(1, 15, 2)],
    # "student": [f"student_{i}" for i in range(1, 15, 2)],
    "age": rng.integers(17, 25, size=7),
    "sex": rng.choice(["male", "female"], size=7)
})
students_df
# jointures de df
# %%
pd.merge(
    note_df, 
    students_df, 
    # how="inner",
    # how="left",
    # how="right",
    # how="outer",
    ## produit cartésien
    # how="cross",
    ## si même nom, inféré par la fonction
    # on="student",
    left_on="student",
    right_on="scholar",
).drop(columns="scholar")
# %%
# merge multiple
from typing import List, Dict, Any, Sequence
# joins = [
#     {"df": pd.Dataframe, "how": str, "on": [str | tuple]},
# ]

def merge_dataframes(from_df: pd.DataFrame, merge_conditions: list[Dict[str, Any]]):
    for join in merge_conditions:
        left_ons, right_ons = [], []
        for key in join["on"]:
            if isinstance(key, str):
                left_ons.append(key)
                right_ons.append(key)
            elif isinstance(key, tuple):
                left_ons.append(key[0])
                right_ons.append(key[1])
        from_df = pd.merge(
            from_df, join["df"], 
            how=join["how"], 
            left_on=left_ons,
            right_on=right_ons
        )
    return from_df

subjects_df = pd.DataFrame({
    "subject": ["biology", "math", "english", "history"],
    "nb_hours": [35, 70, 70, 35]
})

conf = [
    {"df": students_df, "how": "inner", "on": [("student", "scholar")]},
    {"df": subjects_df, "how": "inner", "on": ["subject"]},
]

merge_dataframes(
    from_df=note_df,
    merge_conditions=conf
)


# %%
