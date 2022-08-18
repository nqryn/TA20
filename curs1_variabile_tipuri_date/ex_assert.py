# assert - folosim pentru a verifica o anumita conditie
# Daca conditia este adevarata, codul merge mai departe
# Daca conditia este falsa (adica testul a esuat), codul se opreste si da eroare
anul_nasterii = 1991
varsta = 31

# Verific ca anul nasterii e introdus corect in raport cu varsta
assert 2022 - anul_nasterii == varsta

anul_nasterii = 2001
varsta = 88

# Putem pune dupa virgula un mesaj personalizat de eroare ca sa stim ce nu a mers bine
assert 2022 - anul_nasterii == varsta, f"Anul nasterii este {anul_nasterii}, si nu se potriveste cu varsta {varsta} introdusa!"

# Exemplu cu type casting si verificare ca variabila noua este integer
s1 = "42"
my_int = int(s1)
assert my_int == 42, f"{my_int} nu este in integer egal cu 42"
