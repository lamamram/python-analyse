# %%
print("cell")

# %%
print("other cell")

# %%
# en python, tout est objet
import string

# liste en intension
[ attr for attr in dir(string) if attr.startswith("__") ]
# équivalent à
# for attr in dir(string):
#     if attr.startswith("__"):
#         print(attr)
print(string.__doc__)
# %%
# help(string)
# %%
# l'unpacking de variables
x = 1
y = 2
# équivalent à
t = (1, 2)
x = t[0]
y = t[1]

# équivalent
x, y = [1, 2]
# et
x, y = 1, 2

# %%
def func():
    return "p1", "p2"

x, y = func()
# %%
# formatage
f"1/3 à deux chiffres sign: {1/3:.2f}"
# %%
