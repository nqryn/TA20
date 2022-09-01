# if conditie1:
#     fa ceva daca conditie1 este adevarat
# elif conditie2:
#     fa ceva daca conditie2 este adevarat
# elif conditie3:
#     fa ceva daca conditie3 este adevarat
# else:
#     fa ceva daca nici o conditie de pana acum nu a fost adevarata

varsta = int(input("Varsta:\n"))
if varsta <= 2:
    print("Esti bebelus")
elif varsta <= 12:
    print("Esti copil")
elif varsta <= 18:
    print("Esti adolescent")
elif varsta <= 65:
    print("Esti adult")
else:
    print("Esti pensionar")

if varsta > 65:
    print("pensionar")
elif varsta > 18:
    print("adult")
elif varsta > 12:
    print("adolescent")
elif varsta > 2:
    print("copil")
else:
    print("bebelus")

# if este_lapte_la_magazin:
#     if este_zuzu:
#         cumpara zuzu
#     else:
#         cumpara orice este
# else:
#     asta este, nu mai cumpara nimic

if varsta > 18:
    print("Esti major")
    if varsta > 65:
        print("pensionar")
    else:  # varsta e mai mica decat 65 SI mai mare decat 18
        print("adult")
else:
    print("Esti minor")
    if varsta <= 2:
        print("bebelus")
    elif varsta <= 12:
        print("copil")
    else:  # aici stim ca varsta e mai mare ca 12 SI mai mica decat 18
        print("adolescent")
