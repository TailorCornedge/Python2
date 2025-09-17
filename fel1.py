szam=int(input("Adjon meg egy számot: "))

def eldont():
    if szam % 5 == 0 and szam % 3 == 0:
        return("Ez a szám osztható öttel és hárommal.")
    elif szam % 5 == 0:
        return("Ez a szám osztható öttel.")
    elif szam % 3 == 0:
        return("Ez a szám osztható hárommal.")
    return("Ez a szám nem osztható se öttel, se hárommal.")

print(eldont())