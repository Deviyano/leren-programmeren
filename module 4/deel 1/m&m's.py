import random
lijst=[]
opnieuw=True
thistuple=["oranje","blauw","groen","bruin"]
while opnieuw == True:
    aantal=input("hoeveel M&M's moeten er toegevoegd worden aan de zak?: ")
    try:
        aantal=int(aantal)
        opnieuw=False
    except:
        print("u kunt alleen cijfers invoeren")
        continue
for x in range(aantal):
    lijst.append(random.choice(thistuple))
print(lijst)

