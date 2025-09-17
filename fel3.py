import statistics

class SzamStatisztika:
    def __init__(self, szamok):
        self.szamok = szamok

    def kis_nagy(self):
        nagy = float('-inf')
        kis = float('inf')
        for i in self.szamok:
            if i > nagy:
                nagy = i
            if kis > i:
                kis = i
        return(f"A legkisebb szám: {kis}; a legnagyobb szám: {nagy}")

    def par_parat(self):
        par=0
        parat=0
        for i in self.szamok:
            if i % 2 == 0:
                par+=1
            else:
                parat+=1
        return(f"Páros számok: {par}; páratlan számok: {parat}")
    
    def median(self):
        return(f"A számok mediánja: {statistics.median(self.szamok)}")


szamok=[]

for i in range(7):
    szam=int(input(f"Adja meg a(z) {i+1}. számot: "))
    szamok.append(szam)

statisztika = SzamStatisztika(szamok)

print(statisztika.kis_nagy())
print(statisztika.par_parat())
print(statisztika.median())