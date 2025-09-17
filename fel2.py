lista=[]

for i in range(7):
    szam=int(input(f"Kérem a(z) {i+1}. számot: "))
    lista.append(szam)


nagy=float('-inf')
kis=float('inf')
poz=0
neg=0
nulla=0
for i in lista:
    if i==0:
        nulla+=1
    elif i<0:
        neg+=1
    else:
        poz+=1
    if i>nagy:
        nagy=i
    if kis>i:
        kis=i

print(f"A megadott számok közül {neg} negatív, {poz} pozitív, és {nulla} nulla volt")
print(f"A legnagyobb szám: {nagy}")

print(f"A legkisebb szám: {kis}")
