import random
opnieuw=True
zak=["rood","blauw","groen","geel","bruin"]
while opnieuw == True:
    try:
        aantal=int(input("hoeveel M&M's moeten er toegevoegd worden aan de zak?: "))
        opnieuw=False
    except:
        continue
thisdict ={
"rood":0,
"blauw":0,
"groen":0,
"geel":0,
"bruin":0
}
for x in range(aantal):
    keuze=random.choice(zak)
    thisdict[keuze] = thisdict[keuze]+1
print(thisdict)
