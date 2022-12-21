import random
opnieuw=True
opnieuw2=True
lijst=[]
while opnieuw == True:
    naam = input("Geef een naam op: ").lower()
    if naam =="":
        continue
    if naam in lijst:
        continue
    else:
        lijst.append(naam)
        aantal = len(lijst)
        print(lijst)
    if aantal >= 3:
        opnieuw=False
while opnieuw2== True:
    extra = input("wil je nog meer namen toevoegen: ").lower()
    if extra =="ja":
        naam2 = input("Geef een naam op: ").lower()
        if naam2 in lijst:
            continue
        else:
            lijst.append(naam2)
            continue
    else:
        opnieuw2=False 
for x in range(len(lijst)):
    if len(lijst)<=x+1:
        print(lijst[x],"heeft", lijst[0])
    else:
        print(lijst[x] ,"heeft", lijst[x+1])
