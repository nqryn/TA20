from pprint import pprint
# Dictionar: o structura de date care stocheaza informatii in perechi Key-Value
# unde Key actioneaza ca si indicii de la lista, adica ne permit sa ne referim la Value bazat pe Key

dict_gol = {}

dict1 = {
    "s": 12,
    3: 45,
    3.14: "un alt string",
    True: 5,
    "x": False
}
tren = ["grau", "orz", "orez", "hrisca", "quinoa", "porumb"]
tren_colorat = {
    "rosu": "grau",
    "verde": "orz",
    "albastru": ["orez", "amaranth"],
    "galben": "hrisca",
    "alb": "quinoa",
    "negru": "porumb",
    # "rosu": "amaranth"
}

# Cheile din dictionar trebuie sa fie unice !
# Cheile trebuie sa fie tipuri de date simple (int, float, bool, string)
print(f"In vagonul rosu avem { tren_colorat['rosu'] }")
print(f"In vagonul albastru avem { tren_colorat['albastru'][0] }  si  { tren_colorat['albastru'][1] }")


# Exemplu: vreau sa vad de cate ori apare o litera anume intr-un text
cuvant = "abracadabra"

# daca facem asa, vom avea nevoie de 26 variabile.... cam multe
litera_a_cnt = cuvant.count("a")
litera_b_cnt = cuvant.count("b")

# Facem un dictionar in care key este litera cautata, iar value este de cate ori apare in text
dict_litere_cnt = {
    "a": cuvant.count("a"),
    "b": cuvant.count("b"),
    "r": cuvant.count("r")
}

print(dict_litere_cnt)

# Exemplu: grupare date in mod logic
student_name = "Popescu"
student_firstname = "Ion"
student_age = 21
student_weight = 76.5

student = {
    "name": "Popescu",
    "firstname": "Ion",
    "age": 21,
    "weight": 76.5,
    "birthdate": {
        "day": 19,
        "month": "June",
        "year": 1991
    }
}

print(f"Ma cheama {student['name']} {student['firstname']}. "
      f"Am {student['age']} ani si {student['weight']} kg.")

print(f"M-am nascut pe {student['birthdate']['year']} {student['birthdate']['month']} {student['birthdate']['day']}")

birthdate = student['birthdate']
print(f"M-am nascut pe {birthdate['day']} {birthdate['month']} {birthdate['year']}")

# Operatii pe dictionare
tren_colorat = {
    "rosu": "grau",
    "verde": "orz",
    "albastru": "amaranth",
    "galben": "hrisca",
    "alb": "quinoa",
    "negru": "porumb",
}

# Adaugare element: folosim o cheie care nu mai exista, si elementul e adaugat
tren_colorat['roz'] = "naut"
print(tren_colorat)

# Stergere element
del tren_colorat['roz']
print(tren_colorat)

# Modificare element
tren_colorat['rosu'] = "pietre"
print(tren_colorat)

# pentru a "schimba" Key, trebuie de fapt sa adaugam un nou element cu noua cheie, si sa o stergem pe cea veche
pietre = tren_colorat['rosu']
del tren_colorat['rosu']  # va sterge pietre
tren_colorat['turcoaz'] = pietre
print(tren_colorat)

# Values se pot repeta, nu trebuie sa fie unice
tren_colorat['maro'] = "orz"
tren_colorat['magenta'] = "orz"

# Daca Key nu este in dictionar, cu adresare directa vom primi eroare
print(tren_colorat)
# print(tren_colorat['portocaliu'])  # EROARE, nu este nici un vagon portocaliu
if 'portocaliu' in tren_colorat:  # pot testa daca o Key este in dictionar sau nu
    print(tren_colorat['portocaliu'])
else:
    print("Nu este nici un vagon portocaliu")

# pprint = pretty print
pprint(tren_colorat)
