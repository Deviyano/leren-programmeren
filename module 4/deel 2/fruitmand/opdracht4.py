from fruitmand import fruitmand
import random
lijst=[]
opnieuw=True
while opnieuw == True:
    try:
        aantal=int(input("hoeveel fruit wilt u: "))
    except:
        continue
    for fruit in range(len(fruitmand)):
        lijst.append(fruitmand[fruit]["name"])
        opnieuw=False
    for x in range(aantal):
        print(random.choice(lijst))
        opnieuw=False