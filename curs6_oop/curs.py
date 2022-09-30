from prima_mea_clasa import Person

"""
Clasa este un concept, o suma de caracteristici (atribute) si actiuni (metode).
Fisier: curs_programare.py
"""

class CursProgramare:

    def __init__(self, compania, nume, durata, data_inceput, nr_locuri=10):
        self.compania = compania
        self.nume = nume
        self.durata = durata
        self.data_inceput = data_inceput
        self.nr_locuri_disponibile = nr_locuri
        self.studenti = []

    def inscriere_student(self, student):
        # Aici am putea de exemplu sa verificam daca a trecut data de inceput, si daca nu, sa inscriem studentul
        if self.nr_locuri_disponibile > 0:
            self.studenti.append(student)
            self.nr_locuri_disponibile -= 1
            print(f"Studentul {student.nume} {student.prenume} a fost inscris cu succes")
        else:
            print("Ne pare rau, nu mai sunt locuri disponibile")
        self.descriere_curs()

    def descriere_curs(self):
        print()
        print(f"{self.nume} [{self.compania}] - {self.durata} zile")
        print("-"*80)
        for student in self.studenti:
            print(f"{student.nume} {student.prenume} ({student.varsta})")
        if not self.studenti:
            print("Nu sunt inca studenti inscrisi")
        print()

curs_python = CursProgramare("IT factory", "Introducere in Python", 120, "2023-01-01")
curs_python.descriere_curs()

mihai = Person("Suciu", "Mihai", 22, 1.70)
florian = Person("Chetves", "Florian", 28, 1.90)

curs_python.inscriere_student(mihai)
curs_python.inscriere_student(florian)

print()
curs_python.descriere_curs()

curs_python.inscriere_student(
    Person("Lazarica", "Petrut", 43, 1.80)
)
curs_python.inscriere_student(
    Person("Briceag", "Marcela", 21, 1.60)
)

curs_python.descriere_curs()

