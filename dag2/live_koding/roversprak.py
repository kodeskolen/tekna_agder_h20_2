
# hei -> hohei
# jeg er glad -> jojegog eror gogloladod


# 1. ta inn tekst fra bruker, og skrive ut denne
# 2. hvis en bokstav er en konsonant, legg til 
#    o + konsononat igjen
# 3. hvis ikke, skriv ut bokstaven som vanlig


tekst = input("Skriv inn en tekst: ")

konsonanter = "bcdfghjklmnpqrstvwxz"

for bokstav in tekst:
    if bokstav in konsonanter:
        print(bokstav + "o" + bokstav, end="")
    else:
        print(bokstav, end="")
 



