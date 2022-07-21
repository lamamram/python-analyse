# %%
# la méthode __str__ contrôle le comportement
# d'un objet soumis à str() et donc print()
class Truc:
    def __str__(self) -> str:
        return "machin"
    pass
t = Truc()
print(t)
# %%
# __getitem__ et __setitem__ contrôlent
# l'opérateur [] sur un objet

# getattr et setattr appellent et affectent
# dynamiquement un attribut d'un objet

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
# %%
# paramètres * et ** sur une fonciton
def func(*a, **kwd):
    return a, kwd

func("a", "b", "c", d="d", e="e")

args = ["a", "b", "c"]
kwargs = {'d': 'd', 'e': 'e'}

func(*args, **kwargs)

# %%
import re

zipcode_pattern = "([13456789])([0-9]{4})|2[AB0-9]([0-9]{3})"

target = "44000"

m = re.match(zipcode_pattern, target)
m.group(0)
m.groups()

target = "envoyez à l'adresse: balbal 44000 NANTES ou 75014 PARIS"
re.search(zipcode_pattern, target)
re.findall(zipcode_pattern, target)
list(re.finditer(zipcode_pattern, target))

re.sub(zipcode_pattern, "********", target)
# %%
