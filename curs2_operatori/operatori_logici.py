# Avem 3 operatori logici (functioneaza doar pe variabile boolean): and, or, not
# And - conditie de tip SI: x and y => atat x, cat si y trebuie sa fie adevarat
are_permis = True
varsta = 21

# AND - ambele conditii trebuie sa fie adevarate pentru ca rezultatul sa fie adevarat
assert are_permis and varsta > 18, "Nu ai voie sa conduci o masina"

nota1, nota2, nota3 = 2, 3, 1
# assert nota1 > 4 and nota2 > 4 and nota3 > 4, "Ai picat"

# OR - x sau y: adevarat daca cel putin una dintre conditiile x sau y este adevarata
# assert nota1 > 4 or nota2 > 4 or nota3 > 4, "Nu ai trecut la nici un examen"

# NOT - operatorul de negare: transforma True in False, si viceversa
major = varsta > 18
print(major)
print(not major)
