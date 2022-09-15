"""
1.
Declara o lista note_muzicale in care sa pui do re mi etc pana la do
Afiseaz-o
Inverseaza ordinea folosind slicing si suprascrie aceasta lista
Printeaza varianta actuala (inversata)
Pe aceasta lista, aplica o metoda care banuiesti ca face acelasi lucru, adica sa ii inverseze ordinea. (Nu trebuie sa o suprascrii in acest caz, deoarece metoda face asta automat)
Printeaza varianta actuala a listei. Practic ai ajuns inapoi la varianta initiala

Concluzii: slicing e temporar, daca vrei sa pastrezi noua varianta va trebuie sa suprascrii lista
sau sa o salvezi intr-o lista noua. Metoda gasita de tine, face suprascrierea automat si permanentizeaza
aceste modificari. Ambele variante isi gasesc utilitatea in functie de ce ne dorim in acel moment.
"""
note_muzicale = ["do", "re", "mi", "fa", "sol", "la", "si", "do"]
print(f"1: {note_muzicale}")
note_muzicale = note_muzicale[::-1]  # trebuie sa suprascriem lista originala
print(f"2: {note_muzicale}")
note_muzicale.reverse()  # metoda reverse face acelasi lucru ca si mai sus cu slicing
print(f"3: {note_muzicale}")

# Ar trebui sa ajungem fix la varianta originala (am inversat lista de 2 ori)
assert note_muzicale == ["do", "re", "mi", "fa", "sol", "la", "si", "do"]

"""
2. 
De cate ori apare ‘do’?
"""
count_do = note_muzicale.count("do")  # metoda count numara de cate ori apare termenul cautat in lista
print(f"Do apare de {count_do} ori")
assert count_do == 2

"""
3.
Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4]
Gasiti 2 variante sa le uniti intr-o singura lista.
"""

l1 = [3, 1, 0, 2]
l2 = [6, 5, 4]

#  Varianta 1: adaugare de liste, putem stoca rezultatul intr-o lista noua
lx = l1 + l2

# Varianta2: folosind extend - aceasta metoda modifica lista pe care actioneaza (suprascrie direct)
l1.extend(l2)

# In acest moment, in lx si in l1 ar trebui sa avem aceleasi valori
assert lx == l1

# Se poate folosi si __add__, DAR in general este bine sa evitam metodele cu dublu underscore
# (acestea sunt considerate ascunse, si NU ar trebui folosite)
# l1.__add__(l2)

l1 = [3, 1, 0, 2]
l2 = [6, 5, 4]
# Append este o metoda care adauga un singur element, deci nu o putem folosi pentru unirea a 2 liste
# In cazul acesta, rezultatul va fi [3, 1, 0, 2, [6, 5, 4]], adica o noua lista cu 5 elemente, din care ultimul element este o sublista
l1.append(l2)
print(l1)
print(l1[4])

# In  concluzie, folosim append pentru a adauga un singur element, si extend pentru a adauga toate elementele din alta lista

# Varianta 3: unpack (operatorul *) care reprezinta "despachetarea" valorilor din lista
l1 = [3, 1, 0, 2]
l2 = [6, 5, 4]
new_list = [*l1, *l2]
print(f"Noua lista obtinuta prin unpack este {new_list}")

"""
4.
Sortati si afisati lista generata la ex anterior
Stergeti numarul 0 folosind o functie
Afisati iar lista
"""
lst = [3, 1, 0, 2, 6, 5, 4]
lst.sort()  # Metoda sort functioneaza in-place, adica suprascrie lista originala
print(lst)

# Varianta 1 stergere: folosind remove (trebuie sa dam numarul ce vrem sa il stergem ca argument)
lst.remove(0)

# Varianta 2: folosind del (nerecomandat in felul acesta, in mod normal am cauta indexul elementului pe care vrem sa il stergem)
# Functioneaza doar pentru ca stim ca lista e sortata iar pozitia lui 0 este chiar 0
# del lst[0]

"""
5. 
Folosind un if verificati lista generata la ex3 si afisati
Lista este goala
Lista nu este goala
"""
l = [3, 1, 0, 2, 6, 5, 4]

# Varianta 1: testam direct lista (metoda recomandata)
# Motivul pentru care merge sa facem asa este ca if testeaza valorile ca truthy sau falsey
# Orice colectie python goala va fi falsey, iar orice colectie cu elemente va fi truthy
if l:
    print("Are elemente (truthy)")
else:
    print("Nu are elemente, e goala")

# Varianta 2: testam lungimea (0 - goala)
if len(l) == 0:
    print("Lista e goala, are 0 elemente")
else:
    print("Lista nu e goala")

# Varianta 3: comparatie cu o alta lista goala (NU este recomandat, deoarece construim o noua structura de date inutil)
lista_goala = []
l.clear()  # Golim lista noastra
if l == lista_goala:  # identic cu l ==[]
    print("Lista goala")
else:
    print("Lista plina")


"""
6. 
Folositi o functie care sa stearga lista de la ex3
"""
# Functia pentru golirea unei liste este clear
lst = [1, 2, 3, 4, 5]
lst.clear()  # acum va fi []

# Acum putem adauga inapoi alte elemente, deoarece lista este goala, dar inca exista
lst.append(1)

# Daca vrem sa stergem de tot o lista, adica sa se elibereze din memorie, putem folosi del
del lst
# ATENTIE: in cazul acesta am sters de tot variabila, deci orice altceva incercam sa facem de aici inainte va da eroare
# print(lst)  # EROARE

"""
8. 
Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
Folositi o functie ca sa afisati Elevii (cheile)
"""
dict1 = {
    'Ana': 8,
    'Gigel': 10,
    'Dorel': 5
}
print(dict1.keys())

"""
9. 
Printati cei 3 elevi si notele lor
Ex: ‘Ana a luat nota {x}’
Doar nota o veti lua folosindu-va de cheie
"""
# Varianta 1: accesare directa cu cheile
print(f"Ana a luat nota {dict1['Ana']}")
print(f"Gigel a luat nota {dict1['Gigel']}")
print(f"Dorel a luat nota {dict1['Dorel']}")
# print(f"Viorica a luat nota {dict1['Viorica']}")  # va da eroare, deoarece elevul Viorica nu exista in dictionar

# Varianta 2: cu get (avantajul este ca daca o cheie nu exista, get nu va da eroare)
print(f"Ana a luat nota {dict1.get('Ana')}")
print(f"Gigel a luat nota {dict1.get('Gigel')}")
print(f"Dorel a luat nota {dict1.get('Dorel')}")
print(f"Viorica a luat nota {dict1.get('Viorica')}")  # nu va da eroare

"""
10.
Dorel a facut contestatie si a primit 6
Modificati nota lui Dorel in 6
Printati nota dupa modificare
"""
print(f"Dorel are nota {dict1['Dorel']}")
dict1['Dorel'] = 6
print(f"Dorel a facut contestatie, are acum nota {dict1['Dorel']}")

"""
11.
Gigel se transfera din clasa
Cautati o functie care sa il stearga
Vine un coleg nou. Adaugati Ionica, cu nota 9
Printati noii elevi

"""
dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}

# Varianta 1: del
del dict1['Gigel']

# Varianta 2: pop (diferenta este ca la pop putem sa si obtinem elementul sters)
dict1['Gigel'] = 10
gigel = dict1.pop('Gigel')

# NU folositi __delitem__, este o metoda privata

# Varianta 1 pt adaugare: asignare directa
dict1['Ionica'] = 9

# Varianta 2: folosind update
dict1.update({'Ionica': 9})
# Desi este posibil sa adaugam un element asa, nu este recomandat sa facem asa pentru un singur element
dict1.update({
    'Adela': 5,
    'Ionut': 7,
    'Maria': 10
})

"""
12.
Set
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
Adaugati in zilele_sapt ‘luni’
Afisati zile_sapt
"""
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
print(f"Zilele saptamanii sunt {zile_sapt}")
zile_sapt.add('luni')
print(f"Am adaugat 'luni', acum zilele saptamanii sunt {zile_sapt}")

"""
13.
Folositi un if si verificati daca 
Weekend este un subset al zilelor din sapt
Weekend nu este un subset al zilelor din sapt
"""

# Varianta 1: folosind operatori matematici (<= pentru subset, respectiv >= pentru superset)
if weekend <= zile_sapt:  # puteam folosi si zile_sapt >= weekend
    print("Este subset")
else:
    print("Nu este subset")

# Varianta 2: folosind functia issubset/issuperset (recomandat deoarece este mai explicit)
if weekend.issubset(zile_sapt):  # puteam folosi si zile_sapt.issuperset(weekend)
    print("Este subset")
else:
    print("Nu este subset")

# NU putem folosi in, deoarece in face verificare per element, iar noi avem mai multe elemente de verificat
# element in colectie
print(weekend in zile_sapt)  # va da false

"""
14. 
Afisati diferentele dintre aceste 2 seturi
"""

# Varianta 1: folosind operatorul diferenta - (minus)
print(zile_sapt - weekend)  # vom obtine {'marti', 'joi', 'miercuri', 'vineri', 'luni'}
print(weekend - zile_sapt)  # vom obtine set() - adica un set gol

# Varianta 2: folosind functia difference
print(zile_sapt.difference(weekend))
print(weekend.difference(zile_sapt))

# Rezultatele vor fi DIFERITE, deoarece scaderea NU este comutativa

"""
15.
Afisati intersectia elementelor din aceste 2 seturi
"""
# Varianta 1: folosind metoda intersection
print(zile_sapt.intersection(weekend))
print(weekend.intersection(zile_sapt))

# Varianta 2: folosind operatorul de intersectie &
print(zile_sapt & weekend)
print(weekend & zile_sapt)

# In cazul intersectiei, nu conteaza cum facem, rezultatul va fi acelasi (operatie comutativa)