import math
from abc import ABC
"""
Pilonii OOP (en): inheritance (mostenire), abstraction (abstractizare),
polymorphism (polimorfism) si encapsulation (incapsulare).

2. Abstractizarea: ca si mostenirea, DAR clasa parinte este o clasa abstracta,
adica nu putem face obiecte din ea, si o folosim doar ca si un template
pentru metodele pe care ar trebui sa le implementeze copiii.

Clasa abstracta TREBUIE sa mosteneasca clasa ABC (from abc import ABC).
Fiecare metoda a clasei abstracte trebuie sa arunce exceptia NotImplementedError.
Clasa abstracta NU are constructor, deoarece nu putem face obiecte abstracte.


3. Polimorfism -> poli (mai mult/e) morifs (forma/forme) => ceva care poate lua mai multe forme.
In cazul nostru, o functie de exemplu care desi are acelasi nume, are implementari/definitii diferite.
Exemple: functiile aria si perimetru.

"""

class FormaGeometrica(ABC):

    def aria(self):
        raise NotImplementedError

    def perimetru(self):
        raise NotImplementedError


class Cerc(FormaGeometrica):

    def __init__(self, raza):
        self.r = raza

    def aria(self):
        return self.r**2 * 3.14

    def perimetru(self):
        return self.r * 3.14


class Dreptunghi(FormaGeometrica):
    def aria(self):
        return self.l1 * self.l2

    def perimetru(self):
        return 2*(self.l1 + self.l2)

    def diagonala(self):
        return math.sqrt(self.l1**2 + self.l2**2)

    def __init__(self, lat1, lat2):
        self.l1 = lat1
        self.l2 = lat2

cerc = Cerc(10)
drept = Dreptunghi(4, 6)
print(cerc.aria())
print(drept.aria())

print(cerc.perimetru())
print(drept.perimetru())

lista_fg = [Cerc(4), Dreptunghi(2, 7), Cerc(10), Dreptunghi(5, 5), Dreptunghi(9, 7), Cerc(12)]
for fg in lista_fg:
    print()
    print(f"Perimetru: {fg.perimetru()}")
    print(f"Arie: {fg.aria()}")
