"""
Polimorfism: mai multe functii cu acelasi nume, dar comportament sau parametrii diferit/i.

Metoda language este polimorfica, deoarece returneaza lucruri diferite in functie de obiectul
care o apeleaza, DAR numele metodei este mereu acelasi.
"""

class Romania:

    def language(self):
        return "ro"

class Franta:

    def language(self):
        return "fr"

inst_ro = Romania()
inst_fr = Franta()

print(inst_ro.language())
print(inst_fr.language())


def add(a, b, c=0):
    return a + b

print(add(3, 5))
print(add(2, 4, 6))
