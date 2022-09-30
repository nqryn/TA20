
"""
O clasa este un sablon pe care il folosim ca sa cream "obiecte" din acea clasa.
Obiectele au 2 proprietati importante:
- caracteristici (pe care in clasa le numim ATRIBUTE)
- metode: adica functii definite in interiorul clasei care ne zic noua ce pot face obiectele
"""
class Person:

    nume = ""
    prenume = ""
    varsta = 0
    inaltime = 0.0

    """
    Metoda speciala init este folosita ca si punct de intrare pentru crearea de obiecte
    """
    def __init__(self, name, first_name, age, height):
        self.nume = name
        self.prenume = first_name
        self.varsta = age
        self.inaltime = height

    """
    self este un cuvant cheie care reprezinta obiectul la care ne referim la momentul apelarii metodei
    """
    def present_me(self):
        print(f"Salut, eu sunt {self.nume} {self.prenume} si am {self.varsta} ani")

    def creste_varsta(self):
        self.varsta += 1

# """
# maria si ion sunt OBIECTE create din clasa Person
# """
# maria = Person("Popescu", "Maria", 56, 1.68)
# ion = Person("Marinescu", "Ion", 43, 1.81)
#
# """
# deoarece am folsit clasa Person ca si sablon pentru a crea aceste obiecte,
# putem apela metoda present_me pe ambele.
# """
# maria.present_me()
# ion.present_me()
# print()
#
# gheorghe = Person("Gigi", "Gheo", 21, 1.55)
#
# persoane = [maria, ion, gheorghe]
# for pers in persoane:
#     pers.creste_varsta()
#     pers.present_me()
