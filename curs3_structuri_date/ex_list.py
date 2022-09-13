"""
Listele sunt structuri de date (colectii in Python) care poti tine mai multe valori.
Valorile respective se pot accesa prin INDICE (adica pozitia valorii in lista).
"""
list1 = [5, 7, 12, -3, 8]
list2 = ["Ana", "are", "mere"]
list3 = [True, False, False, True, False, False, False]

#          0       1     2         3        4         5
tren = ["grau", "orz", "orez", "hrisca", "quinoa", "porumb"]
print(f"In vagonul 1 avem {tren[1]}")
print(tren[1:4])  # slicing functioneaza pe liste exact ca si la stringuri
print(f"In ultimul vagon avem {tren[-1]}")  # indexare negativa
print(f"Trenul are in total {len(tren)} vagoane!")  # lungimea listei se determina cu functia len

# Pentru a adauga elemente noi in lista, folosim o functia numita append
print(tren)
tren.append("ovaz")
print(tren, len(tren))

print("_"*100)
# Listele nu trebuie obligatoriu sa aiba elemente cu acelasi tip
lista_complexa = ["un string", True, 12, "alt string", 3.14, "alt string"]

print(lista_complexa)
lista_complexa.remove("alt string")  # stergere un element din lista bazat pe valoare
print(lista_complexa)

var_pop = lista_complexa.pop(1)
print(f"Am scos din lista, de la indicele 1, valoarea {var_pop}")
print(lista_complexa)

lista_complexa.clear()  # sterge toate elementele din lista
print(lista_complexa)

del lista_complexa  # sterge VARIABILA lista_complexa
# print(lista_complexa)  # va da eroare, deoarece am sters lista de tot

#    0     1    2    3    4    5    6    7
l = ["a", "b", "c", "a", "b", "x", "z", "b"]
index_primul_b = l.index("b")  # returneaza indexul la care gasim valoarea din paranteze
print(index_primul_b)
# ca sa gasim al doilea b, trebuie sa facem slicing, si sa incepem cautarea de la pozitia primului + 1
# deoarece prin slicing avem o NOUA lista, mai scurta, vom obtine un index mai mic decat cel real
# pentru a rezolva problema asta, trebuie sa tinem cont ca sunt `index primul b + 1` elemente pe care nu le luam in considerare
print(f"Cautam acum cu slicing in sub-lista {l[index_primul_b + 1:]}")
#  0    1    2    3    4    5
# "c", "a", "b", "x", "z", "b"]
# in sub-lista, al doilea b va fi la pozitia 2
# dar sub-lista noastra, comparat cu lista originala, este mai scurta cu 2 elemente
# ceea ce inseamna ca in lista originala al doilea b se gaseste la pozitia 4
index_al_doilea_b = l[index_primul_b + 1:].index("b") + index_primul_b + 1
print(index_al_doilea_b)
index_al_treilea_b = l[index_al_doilea_b + 1:].index("b") + index_al_doilea_b + 1
print(index_al_treilea_b)

# Deoarece putem sa adaugam/stergem/modificam elementele din lista, zicem ca lista e MUTABILA
l[0] = l[0].upper()
l[1] = l[1].upper()

print(l)

# Functii pe liste: max, min, sum
lx = [5, 7, 12, -3, 8, 2, 3, 21]
print(max(lx))
print(min(lx))
print(sum(lx))

# List membership: verificare daca o valoare se gaseste intr-o lista
print(7 in lx)  # True
print(6 in lx)  # False

vocale = ['a', 'e', 'i', 'o', 'u']
litera = input("Litera:\n")

if litera == 'a' or litera == 'e' or litera == 'i' or litera == 'o' or litera == 'u':
    print("Litera este vocala")

if litera in vocale:
    print("Litera este vocala")


# Concatenarea (adunarea) a doua liste
ly = [70, 33, 14, 51]
lz = lx + ly
print(f"LX: {lx}\nLY: {ly}")
print(lz)

# A doua modalitate este cu metoda extend (se va modifica lista pe care facem extend)
lx.extend(ly)
print(f"LX este acum: {lx}")