from fruitmand import fruitmand
import random
lijst=[]
aantal=int(input("hoeveel fruit wilt u: "))
for fruit in range(len(fruitmand)):
    lijst.append(fruitmand[fruit]["name"])
for x in range(aantal):
        print(random.choice(lijst))