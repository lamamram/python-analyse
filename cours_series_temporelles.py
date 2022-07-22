# %%
import os
import pandas as pd
from time import time
import numpy as np
import matplotlib.pyplot as plt

print(pd.__version__)
print(np.__version__)

# instanciation correcte d'un rng
rng = np.random.default_rng(int(time()))

# %%

def get_temps(offset):
    return (list(np.around(rng.uniform(-4. + offset, 5. + offset, size=6), 1))
        + list(np.around(rng.uniform(4. + offset, 15. + offset, size=6), 1))
        + list(np.around(rng.uniform(12. + offset, 30. + offset, size=6), 1)))

get_temps(-2)
# %%
dates = pd.Series(["2022-01-01", "2022-07-01"])
dates

# conversion et attribut dt
dates = dates.astype("datetime64")
dates.dt.year
dates.dt.strftime("%d/%m/%Y")
# %%
# date_range
index = pd.date_range(dates[0], dates[1])
index
# %%
index = pd.date_range(dates[0], dates[1], freq="15D")
index
# %%
# fin du mois
pd.date_range(dates[0], dates[1], freq="M")
# début du mois
pd.date_range(dates[0], dates[1], freq="MS")

# date de départ + nb +frq
pd.date_range(dates[0], 6, freq="MS")
# %%
# mis et années
pd.period_range(dates[0], dates[1], freq="M")
# %%
# 1er et 15 du mois
index = pd.date_range("2022-01-01", periods=9, freq="MS")
ides = index + pd.Timedelta("14D")
index = index.union(ides)
index
# %%
temps_df = pd.DataFrame({
    "Lille": get_temps(-2),
    "Nantes": get_temps(0),
    "Toulouse": get_temps(5)
}, index=index)

temps_df = temps_df.stack().reset_index()
temps_df.rename(columns={
    "level_0": "index",
    "level_1": "city",
    0: "temp"
}, inplace=True)
temps_df
# %%
temps_df.pivot(
    index="index",
    columns="city",
    values="temp"
).plot()

# %%
