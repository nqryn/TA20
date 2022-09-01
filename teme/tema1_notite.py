"""
Metodele cu dublu underscore (gen __len__) sunt considerate private si nu ar trebui folosite in cod.
Pentru fiecare metoda de genul acesta, avem o alta optiune recomandata.
"""
nume = "Adela"
print(nume.__len__())  # Asa NU, desi functioneaza, dar nu e recomandat
print(len(nume))  # Asa DA

print(nume[2])  # va afisa e, al 3lea caracter din sir
# A d e l a
# 0 1 2 3 4
print(nume[1:3])  # va printa de
# str[start:stop:pas] pas e in mod implicit 1

# len(nume) va fi 5, deci slicing-ul nostru va lua in considerare si ultimul caracter din string
print(nume[0:len(nume):2])  # va printa Aea
print(nume[ :len(nume):2])
print(nume[0: :2])
print(nume[ : :2])
# Cele 4 instructiuni de mai sus sunt echivalente, deoarece in slicing putem omite capetele stringului (sunt implicite)

# Putem avea si valori negative la indexare/slicing
print(nume[-1])  # nume[len(nume)-1] -> a
print(nume[-2])  # l
print(nume[-3])  # e

print(nume[::-1])  # sirul inversat, putem avea pas negativ

"""
Metoda split functioneaza pe stringuri, si le imparte in bucati.
Implicit, aceasta imparte stringurile dupa spatiile goale.
Daca dorim impartire dupa alt caracter, trebuie sa il transmitem ca argument.
"""
name = "Kacso-Vidrean Elena-Adela"
last_name, first_name = name.split()
print(last_name)  # Kacso-Vidrean
print(first_name)  # Elena-Adela
middle_name, first_name = first_name.split("-")
print(middle_name)  # Elena
print(first_name)  # Adela


"""
Atunci cand avem o variabila intre ghilimele, aceasta va fi intotdeauna string.
Chiar daca continutul ei este int, float, bool, etc.
Pentru a verifica tipul valorilor din interiorul stringului, avem nevoie de functii speciale, sau de type casting.
"""
s = "1234"
print(type(s))  # va printa string

s = "12.34"
print(type(s))

s = "True"
print(type(s))

# Nu putem compara variabilele de mai sus cu int/float/bool
s = "42"
# assert s == int  # <- va da eroare, nu asa verificam daca este intr-adevar un boolean
assert s.isdigit()  # OK
assert s.isnumeric()  # OK
assert int(s) == 42  # OK
assert isinstance(s, int)  # NU va merge, deoarece type este string


"""
Metode pe string
"""
s = "The coral is either the smartest rock or the stupidest animal. How are you?"
d = "1234"
print(s.isdigit())
print(d.isdigit())

prima_propozitie, a_doua_propozitie = s.split(".")
print(prima_propozitie + ".")
print(a_doua_propozitie)

print(F"Litera e apare de {s.count('e')} ori")
print(f"Substringul 'the' apare de {s.count('the')}")
print(f"Cuvantul 'the' apare de {s.count(' the ')}")

print(s.index('the'))  # va afisa indexul la care gaseste prima data substringul `the`
print(s.upper())
print(s.lower())

print(s.replace("the", "***"))  # Va inlocui `the` cu `***` peste tot in stringul s
print(s)

print(s.partition("."))  # spre deosebire de split, va returna si caracterul dupa care facem split, adica punctul


"""
6. Citește de la tastatură:
- numele;
- prenumele.
Afișează: 'Numele complet are x caractere'.
"""
nume = input("Nume:\n")
prenume = input("Prenume:\n")

# Asta merge doar daca avem un singur nume si un singur prenume
# nume, prenume = input("Introdu numele si prenumele separate de spatii:\n").split()
print(f"Numele complet are {len(nume) + len(prenume)} caractere")
print(f"Numele complet are {len(nume + prenume)} caractere")

b = True
print("Salut " + str(b))
print(f"Salut {b}")
# nu putem face asa
# print("Salut" + b)

s = "56"
assert s.isdigit(), f"Mesaj de eroare"

# Exercitii optionale (mai grele)
print('=' * 80)

# Obtinere mijloc string pt lungime impara
# Exemplu string cu lungime 7 (ultimul index va fi 6, deoarece pornim de la 0) => mijlocul este indexul 3
# Putem ori sa scadem 1 din lungime inainte sa impartim la 2, ori sa folosim o metoda de rotunjire
# 0 1 2 3 4 5 6
# c u v i n t e
sentence = "cuvinte"
index_mijloc = (len(sentence) - 1) / 2  # impartire simpla
index_mijloc = len(sentence) // 2  # daca folosim // se va face impartire fara rest, adica 7 / 2 va da 3.5, dar 7 // 2 va da 3
print(sentence[index_mijloc])  # va printa i

# Palidrom: un string care se citeste la fel din ambele capete, ex alabala
palidrom = input("Introduceti un cuvant pt a verifica daca e palindrom")
assert palidrom == palidrom[::-1]

# Compunere operatii de input + split
cuvant1, cuvant2 = input("Introdu 2 cuvinte separate de spatiu (ex. alabala portocala)").split()
print(cuvant1)
print(cuvant2)

# In viata reala, nu ne vom baza niciodata pe faptul ca utilizatorul va scrie fix 2 cuvinte, si vom face MEREU verificari
cuvinte = input("Introdu 2 cuvinte separate de spatiu (ex. alabala portocala)")
assert cuvinte.split() == 2, "Ai introdus un alt numar de cuvinte decat cel cerut!!"
