import random
Zak=["rood","blauw","groen","geel","bruin"]
aantal=int(input("hoeveel M&M's moeten er toegevoegd worden aan de zak?: "))
thisdict ={
"rood":0,
"blauw":0,
"groen":0,
"geel":0,
"bruin":0
}
for x in range(aantal):
    keuze=random.choice(Zak)
    thisdict[keuze] = thisdict[keuze]+1
print(thisdict)
