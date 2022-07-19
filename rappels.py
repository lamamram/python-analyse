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

# copie indépendante en mémoire pour les types list et dict
rows2 = rows.copy()
rows.sort()
print(rows)
print(rows2)
del rows2
# %%

# chainage de méthodes

class Truc:
    def transfo1(self):
        print("trasfo1")
        return self
    
    def transfo2(self):
        print("trasfo2")
        return self

t = Truc()
t.transfo1().transfo2()
# %%
class Truc:
    def __str__(self) -> str:
        return "machin"
    pass
t = Truc()
print(t)
# %%
# ajout d'un élément à une séquence
lst = [1, 2]
lst.append(3)
lst

# concatenation d'un liste
lst + [4, 5]
lst.extend([4, 5])
lst
# %%

from datetime import datetime, timedelta

dt = datetime(2022, 7, 18, 16, 18, 33)

dt = datetime.now()
dt

dt = datetime.strptime("2022-07-18 16:19:22", "%Y-%m-%d %H:%M:%S")
dt

dt.strftime("%d/%m/%Y")

dur = datetime.now() - dt
dur

cuisson_oeuf_coque = timedelta(minutes=3)
datetime.now() + cuisson_oeuf_coque

# %%

# équivalences entre liste de tuples et dictionnaire

keys = ["k1", "k2"]
values = ["v1", "v2"]

list(zip(keys, values))
d = dict(zip(keys, values))

for k, v in d.items():
    print(k, v)
# %%
# %%

class Truc:
    def __init__(self, param):
        self.param = param
    
    def __setitem__(self, param, value):
        setattr(self, param, value)
    
    def __getitem__(self, param):
        return getattr(self, param)
    
    def func(self):
        return "hello"
    


t = Truc("value")
print(t.param)
print(t["param"])
t["param"] = "new_val"
print(t.param)

print(getattr(t, "func")())
# %%
# annotations
# 1. action purement informative (pas de contrôlle de type)
# 2. permet l'autocomplétion dans l'éditeur
def func(p1: int, p2: str) -> tuple:
    return p1, p2

print(func.__annotations__)
func("hi", 0)
# %%

def add_elem(elem, lst):
    lst.append(elem)

l = [1, 2, 3]
add_elem(4, l)
print(l)
# %%
