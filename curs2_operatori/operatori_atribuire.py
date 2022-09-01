a = 10  # operatorul standard de atribuire
a += 2  # echivalent cu a = a + 2
a -= 2  # a = a - 2
a *= 2  # a = a * 2
a /= 2  # a = a / 2 =>  aici a va deveni 10.0, deoarece impartirea normala da mereu un float
print(a)

a = int(a)
a //= 2  # Operatorul // este pentru impartire FARA REST (impartire intreaga)
print(a)

print(7 / 2)  # va printa 3.5
print(7 // 2)  # va printa 3
