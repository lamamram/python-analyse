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
# valeur à l'indice, indice d'une valeur
lst = [1, 2, 3]
lst[0]
lst.index(1)
# %%
x = x + 1
# pour tous les opérateurs arithmétiques
x += 1

# %%
# fonctions lambda: mauvaise utilisation
# une lambda est une fonction sans nom, donc à usage unique
# associant des paramètres à une expression de retour
# équivalent à 
x = 10
if x > 5:
    x **= 2
else:
    x -= 1 

func = lambda x: x**2 if x > 5 else x - 1
func(4)
# %%
# programmation fonctionnelle:
# map exécute une fonction sur tous les éléments d'un itérable
squares = list(map(lambda x: x**2, [1, 2, 3, 4]))
squares
# %%
odds = list(filter(lambda x: x%2, [1, 2, 3, 4]))
odds

# %%
rows = [f"row_{i}" for i in range(15)]
rows
sorted(rows)
sorted(rows, key=lambda r: int(r[4:]))

# %%
