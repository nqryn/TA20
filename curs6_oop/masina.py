
"""
Numele de clase se scriu mereu cu litera mare la inceput (CamelCase)
spre deosebire de variabile care sunt snake_case
"""
class Burger:

    def __init__(self, ingrediente, sos, vegetarian=False):
        self.ingrediente = ingrediente
        self.sos = sos
        self.vegetarian = vegetarian

    def reteta(self):
        print("Prajiti chifla")
        print("Puneti partea de jos a chiflei pe o farfurie")
        if self.vegetarian:
            print("Adaugati o bucata prajita de halloumi")
        else:
            print("Adaugati o bucata de vita Angus")
        for ingredient in self.ingrediente:
            ingredient.gateste()
        print(f"Turnati mult sos {self.sos} peste ingrediente")
        print("Puneti partea de sus a chiflei peste burger")
        print("Serviti cald!")
        print()


"""
In mod normal, fiecare clasa se defineste in fisierul ei
Numele fisierului trebuie sa fie reprezentativ pentru clasa
ingredient.py
"""

class Ingredient:

    def __init__(self, nume, metoda_gatire):
        self.nume = nume
        self.metoda_gatire = metoda_gatire

    def gateste(self):
        print(f"Ingredient: {self.nume}")
        print(f"\t{self.metoda_gatire}")

cheddar = Ingredient("Cheddar", "taiati in felii si puneti peste burger")
ceapa_caram = Ingredient("Ceapa", "prajiti in ulei pana cand devine dulce, apoi puneti peste burger")
castraveti_murati = Ingredient("Castraveti murati", "deschideti borcanul, taiati castravetii felii, si puneti peste burger")
rosii = Ingredient("Rosii", "taiati in felii si puneti peste burger")

burger = Burger([cheddar, ceapa_caram, castraveti_murati], "BBQ")
burger.reteta()

burger_vegetarian = Burger([cheddar, rosii, castraveti_murati], "Remoulade", True)
burger_vegetarian.reteta()


# class Test:
#
#     def __init__(self, url):
#         pass
#
#     def setup(self):
#         self.maximize

# l este obiectul, list este clasa
l = list()
# cand apelam o metoda pe obiect, l devine self
l.append(2)