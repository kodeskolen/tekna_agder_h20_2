
mnd = ["januar", "februar", "mars", "april", "mai",
       "juni", "juli", "august", "september",
       "oktober", "november", "desember"]

for måned in mnd:
    print(måned)

tmp = [-10, -5.5, 0.3, 5.5, 10.4, 12.8, 16.1, 15.3,
       10.1, 8.7, 4.2, -1.3]

gjennomsnitt = 0

for temperatur in tmp:
    gjennomsnitt += temperatur

gjennomsnitt /= len(tmp)

print(f"Gjennomsnittet er {gjennomsnitt:.2f} grader.")

for (måned, temperatur) in zip(mnd, tmp):
    print(f"{måned}: {temperatur}")





