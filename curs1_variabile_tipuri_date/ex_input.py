# Input - functia cu care preluam date de la utlizator (de la tastatura)
# \n - newline, adica ducem cursorul pe urmatoarea linie, ca sa arate frumos
nume = input("Introdu numele:\n")

print(f"Salut, {nume}!")

# By default, ce primim noi de la input este INTOTDEAUNA string
varsta = input("Cati ani ai?\n")
print(type(varsta))

# Daca dorim alte tipuri de date, trebuie sa face type casting!
varsta = int(varsta)
print(type(varsta))

# Exercitiu cu assert si input : cod captcha
x, y = 5, 17  # dam valori dinamice lui x si y, ca sa le putem schimba la fiecare rulare daca vrem
rezultat_captcha = int(input(f"Cat este {x} + {y}?\n"))
assert rezultat_captcha == x + y, "Nu esti om, esti robot!"
