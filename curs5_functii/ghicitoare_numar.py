import random
"""
13.
Ghicitoare de numar
numar_secret = Generati un numar random intre 1 si 30
Numar_ghicit = None
Folosind un while
   User alege un numar
   Programul ii spune:
Nr secret e mai mare
Nr secret e mai mic
Felicitari! Ai ghicit!

"""

# Functia ai_ghicit va returna True daca s-a ghicit numarul, si False altfel. Va si afisa mesajul de "mai mic", "mai mare"
def ai_ghicit(nr_secret, nr_ghicit):
    if nr_secret == nr_ghicit:
        print("Felicitari! Ai ghicit!")
        return True

    if nr_ghicit > nr_secret:
        print(f"Nr secret e mai mic decat {nr_ghicit}, mai incearca")
    else:
        print(f"Nr secret e mai mare decat {nr_ghicit}, mai incearca")
    return False

numar_secret = random.randint(1, 30)  # alegem un numar aleator intre 1 si 30
incercari = 0
max_incercari = 5
while incercari < max_incercari:
    incercari += 1
    numar_ghicit = int(input("Ghiceste:\n"))
    if ai_ghicit(numar_secret, numar_ghicit):
        print(f"Ai ghicit din {incercari} incercari!")
        break
else:
    # Aici se va ajunge doar daca while nu a ajuns deloc la un break
    print(f"Nu ai ghicit din {max_incercari} incercari, jocul s-a terminat. Ai pierdut!")
