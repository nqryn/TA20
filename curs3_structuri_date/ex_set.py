# Set = structura de date (colectie) care are doar elemente unice

set_gol = {}  # NU putem face asa, asta e un dictionar
set_gol = set()
print(set_gol)

an = {'primavara', 'vara', 'toamna', 'iarna'}
print(an)

an.add('primavara')
print(an)

an.add('ceva')
print(an)

# print(an[0])  # EROARE, nu pot accesa asa un set

# Set membership
anotimp = "vara"
if anotimp in an:
    print("Gasit")
else:
    print("Nu exista in set")

an.remove('vara')
print(an)

if anotimp in an:
    print("Gasit")
else:
    print("Nu exista in set")

print(f"Lungimea setului este {len(an)}")
