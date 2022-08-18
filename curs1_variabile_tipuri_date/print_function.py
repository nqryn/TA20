varsta = 25
prenume = "Adela "
nume = "Neacsu"

# Print este o functie care "scrie" in consola, dar care asteapta stringuri
print("Pe mine ma cheama " + prenume + nume)
print("Eu am " + str(varsta) + " ani")  # Nu putem concatena varsta(int) cu str, deci trebuie sa facem type casting

# F-strings (formatted strings)
print(f"Pe mine ma cheama {prenume} {nume} si am {varsta} ani!")  # este varianta recomandata de a folosi print
# print(f"Ce se intampla {prenume, nume}")  # aici se creeaza o tupla (nu folositi inca acest format)

print(f"Am mai crescut un an, acum am {varsta + 1} ani!")

var_str = f"Aici voi scrie mult text.... kfdlfkld vclvkd Autor: {prenume} {nume}"
var_str += f"Am scris si voi mai scrie baldjfisdnfds fsfnjdfosdnfd {varsta}"
var_str += "Si atat!"

print(var_str)

print(f'Ghilimele simple {nume}')

