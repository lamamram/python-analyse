# %%
# exo: à partir de l'url suivante: 
# http://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv
# analyser les données
# calculer le nb, la somme et le pourcentage de survivants chez les femmes et les enfants par classe
# hint: le groupby est une opération couteuse en ressources
# il est donc préférable de se donner un dataframe réduit aux données utiles en premier lieu
import numpy as np
import pandas as pd

from utils import percent_agg

titanic_df = pd.read_csv("http://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv")
titanic_df
# %%
is_wmn_or_child = titanic_df["who"].isin(["woman", "child"])
sub_df = titanic_df.loc[is_wmn_or_child, ["survived", "pclass", "who"]]

sub_df
# %%
gb = sub_df.groupby(["pclass", "who"])

gb.agg({"survived": ["count", "sum", percent_agg]})
# %%
