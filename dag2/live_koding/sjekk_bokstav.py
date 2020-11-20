

mnd = ["januar", "februar", "mars", "april",
       "mai", "juni", "juli", "august",
       "september", "oktober", "november", "desember"]

bokstav = "r"

for måned in mnd:
    if bokstav in måned:
        print(f"Bokstaven {bokstav} er i ordet {måned}. " \
              + "Du burde ta tran i denne måneden!")
