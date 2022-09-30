# """
# 2. Functie care sa returneze TRUE daca un numar este par, FALSE pt impar
# """
# # atentie la cum alegem numele functiilor
# # folosim verbe, incercam sa evidentiem ce o sa returnam, si sa fim cat mai clari in denumire
# def este_nr_par(nr):  # sau este_par, sau is_even
#     if nr % 2 == 0:
#         return True
#     else:
#         return False
#
# # print(f"Pentru valorarea 5, functia par_imapar returneaza {par_impar(5)}")
# # print(f"Pentru valorarea 6, functia par_imapar returneaza {par_impar(6)}")
#
# """
# 3. Functie care returneaza numarul total de caractere din numele tau complet.
# (nume, prenume, nume_mijlociu)
# """
# def calculeaza_lungime_totala(nume, prenume, nume_mijlociu=""):
#     return len(nume) + len(prenume) + len(nume_mijlociu)
#
# print(calculeaza_lungime_totala("Neacsu", "Adela", "Elena"))
# print(calculeaza_lungime_totala("Popescu", "Ion"))
#
# """
# 6. Functie care returneaza True daca un caracter x se gaseste intr-un string dat. False daca nu
# """
#
# def is_in_string(my_char, my_str):
#     for c in my_str:
#         if c == my_char:
#             return True  # iesim din functie daca gasim caracterul cautat, nu are rost sa mai cautam
#     return False  # daca am ajuns aici, inseamna ca nu am gasit deloc caracterul cautat
#
# # variabilele definite in afara oricarei functii se numesc GLOBALE
# # astfel, avem acces la ele si in interiorul functiei
# # DAR nu e ok sa facem asa, si variabilele de care avem nevoie in functie ar trebuie MEREU
# # sa fie transmise prin parametri!!
# def preia_date_utilizator():
#     my_str = input("String:\n")
#     my_char = input("Char:\n")
#     is_in_string(my_char, my_str)
#
#
# """
# 7. Functie fara return, primeste un string si printeaza pe ecran:
# Nr de caractere lower case este x
# Nr de caractere upper case exte y
# """
# def print_lower_upper_counters(s):
#     cnt_low = 0
#     cnt_upp = 0
#     for c in s:
#         if c.isupper():
#             cnt_upp += 1
#         if c.islower():
#             cnt_low += 1
#     print(f"Nr de caractere lower case este {cnt_low}")
#     print(f"Nr de caractere upper case este {cnt_upp}")
#
# """
# 8. Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive
# """
# def get_positives(init_list):
#     positives = []
#     for nr in init_list:
#         if nr >= 0:
#             positives.append(nr)
#     return positives
#
# """
# 10. Functie care primeste un numar si un set de numere.
# Printeaza ‘am adaugat numarul nou in set’ + returneaza True
# Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza Fals
# """
# # NU denumiti variabilele set, dict, list, etc.
# def add_to_set(nr, my_set):
#     if nr in my_set:
#         print("nu am adaugat numarul in set. Acesta exista deja")
#         return False
#     else:
#         my_set.add(nr)
#         print("am adaugat numarul nou in set")
#         return True
#
# add_to_set(1, {2, 3, 4})

"""
12. Functie calculator care sa returneze 4 valori
Suma, diferenta, inmultirea, impartirea a 2 numere
"""

# atunci cand returnam mai multe valori dintr-o functie, acestea sunt puse automat intr-un tuple
def calculator(a, b):
    return a+b, a-b, a*b, a/b

rezultat = calculator(12, 5)
print(rezultat)

s, d, p, c = calculator(17, 4)
print(f"Suma: {s}, Diferenta: {d}, Produsul: {p}, Catul: {c}")