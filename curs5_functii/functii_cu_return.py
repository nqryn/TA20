"""
Return - valoarea returnata => o valoare pe care o functie o da inapoi la apelare.

def func_name(ceva):
    ...
    cod
    ...
    return altceva

"""

# Functia contor
# Primeste ca si parametri: o lista in care sa caute, si elementul cautat
# Returneaza : de cate ori apare elemntul cautat in lista

def contor(lista_nr, element_cautat):
    contor_element = 0
    # Pentru fiecare numar `nr` din lista noastra
    for nr in lista_nr:
        # Daca numarul curent `nr` este egal cu numarul cautat
        if element_cautat == nr:
            # Incrementam contorul
            contor_element += 1

    print(f"Am terminat de cautat, am gasit ca {element_cautat} apare de {contor_element} ori in lista!")
    return contor_element

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
contor_3 = contor(numere, 3)
print(f"Am primit rezultatul de la functie, este {contor_3}!")
print()

"""
Return (rezultatul) este optional.
Dar putem avea si mai multe instructiuni de tip return, INSA doar una dintre ele va fi activa la o apelare,
deoarece atunci cand Python gaseste un return, OPRESTE functia.
"""
def functie_cu_multireturn(varsta):
    if varsta < 18:
        return "minor"
    elif varsta < 65:
        return "adult angajat"
    else:
        return "pensionar"

ionel = functie_cu_multireturn(54)
print(ionel)
maria = functie_cu_multireturn(15)
print(maria)

def functia_mea():
    print("Am intrat in functie...")
    return 100
    print("Aici nu se mai ajunge...")

functia_mea()