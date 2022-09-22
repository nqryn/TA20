"""1.
Avand lista
    masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

Folositi un for ca sa iterati prin toata lista si sa afisati
‘Masina mea preferata este x’
Faceti acelasi lucru cu un for each
Faceti acelasi lucru cu un while
"""
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

# for simplu (cu range)
for i in range(len(masini)):
    print(f"{i}: Masina mea preferata este {masini[i]}")
print()

# for each
for masina in masini:
    print(f"Masina mea preferata este {masina}")
print()

# while
contor = 0
while contor < len(masini):
    print(f"Masina mea preferata este {masini[contor]}")
    contor += 1  # incrementare
print()

"""2.
Aceeasi lista
Folositi un for
In for
   Modificati elementele din lista astfel incat sa fie scrie cu majuscule, exceptand primul si ultimul
Printati varianta finala a listei
"""
for i in range(len(masini)):
    # daca e prima sau ultima masina, NU o facem cu majuscule
    if i == 0 or i == len(masini)-1:
        continue
    masini[i] = masini[i].upper()
print(masini)
print()

"""3. 
Aceeasi lista, 
Vine un cumparator care doreste sa cumpere un Mercedes
Iterati prin ea prin for each
Daca masina e mercedes (if)
   Printam ‘am gasit masina dorita de dvs’
   Iesim din ciclu folosind un cuvant cheie care face acest lucru
Altfel
   Printam Am gasit masina X. Mai cautam	
"""
masina_dorita = "Mercedes"
for masina in masini:
    # comparam ambele stringuri cu litere mici, ca sa nu fie probleme cu case-ul
    if masina.lower() == masina_dorita.lower():
        print("am gasit masina dorita de dvs")
        break
    else:
        print(f"Am gasit masina {masina}. Mai cautam")
print()

"""4.
Aceasi lista
Vine un cumparator bogat dar indecis. Ii vom prezenta toate masinile cu exceptia Trabant si Lastun. 
Daca masina e Trabant sau Lastun
   Folositi un cuvant cheie care sa dea skip la ce urmeaza
Printati S-ar putea sa va placa masina x
"""
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for masina in masini:
    if masina == "Trabant" or masina == "Lastun":
        continue
    print(f"S-ar putea sa va placa masina {masina}")
print()


"""5. 
Modernizati parcul de masini
Creati o lista goala, masini_vechi
Iterati prin masini
Cand gasiti Lastun sau Trabant:
Salvati aceste masini in masini_vechi
Suprascrieti-le cu ‘Tesla’ (in lista initiala de masini)
Printati Modele vechi: x
Modele noi: x
"""
masini_vechi = []
print(f"Lista init: {masini}")
for i in range(len(masini)):
    if masini[i] == "Lastun" or masini[i] == "Trabant":
        masini_vechi.append(masini[i])
        masini[i] = "Tesla"
print(f"Modele vechi: {masini_vechi}")
print(f"Modele noi: {masini}")
print()

"""6. 
Avand dict
pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
Vine un client cu un buget de 15000 euro
Prezentati doar masinile care se incadreaza in acest buget
Iterati prin dict.items() si accesati masina si pretul
Printati Pentru un buget de sub 15000 euro puteti alege masina x
Iterati prin lista
"""
pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000,
    'Jeep': 15000
}
buget = 15000
for marca, pret in pret_masini.items():
    if buget >= pret:
        print(f"Pentru un buget de sub {buget} euro puteti alege masina {marca}")

print()

"""7.
Avand lista
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
Iterati prin ea
Afisati de cate ori apare 3
(nu aveti voie sa folositi count)
"""
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
contor_3 = 0
for nr in numere:
    if nr == 3:
        contor_3 += 1  # incrementam contorul atunci cand gasim un 3
print(f"Am gasit numarul 3 de {contor_3} ori!")

"""8. 
Aceeasi lista
Iterati prin ea
Calculati si afisati suma numerelor
(nu aveti voie sa folositi sum)
"""
suma = 0
for nr in numere:
    suma += nr
print(f"Suma numerelor din lista este {suma}!")

"""9. 
Aceeasi lista
Iterati prin ea
Afisati cel mai mare numar
(nu aveti voie sa folositi max)
"""
# nr_max = 0  # sa nu faceti asta decat daca sunteti 100% siguri ca lista are doar numere pozitive
nr_max = numere[0]  # preferam sa luam primul element din lista
for nr in numere:
    if nr > nr_max:
        nr_max = nr
print(f"Maxim: {nr_max}")
print()

"""10.
Aceeasi lista
Iterati prin ea
Daca numarul e pozitiv, inlocuiti-l cu valoarea lui negativa
Ex: daca e 3, sa devina -3
Afisati noua lista
"""
print(numere)
for i in range(len(numere)):
    if numere[i] > 0:
        numere[i] = -numere[i]
print(numere)

lista_negative = [-5, -7, -3, -9, -3, -3, -1, -4, -3]
maxim = 0  # va da un rezultat gresit, deoarece 0 este deja mai mare decat toate numerele din lista
for nr in lista_negative:
    if nr > maxim:
        maxim = nr
print(f"Am gasit maximul in lista {maxim}, iar functia max mi l-a gasit {max(lista_negative)}")
