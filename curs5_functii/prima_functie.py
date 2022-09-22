"""
Functii - bucati de cod reutilizabile pe care oricine le poate folosi.
Adica noi definim o functie o data, si apoi o putem folosi in mai multe locuri.

Sintaxa

def nume_functie( optional, aici putem avea parametri ):
    aici, indentat
    va fi
    corpul functiei
    adica tot ceea ce se executa
    in functie

Cat timp doar definim o functie, nimic nu se intampla. Trebuie sa o APELAM pentru ca codul din interior sa se execute!
"""
def say_hello():
    print("1. Hello")
    print("2. Aceasta este prima mea functie!!!!")

print("3. Azi vom invata despre functii!")
say_hello()

