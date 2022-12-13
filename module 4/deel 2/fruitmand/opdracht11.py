from fruitmand import fruitmand
loop = True
kleuren = []
naam = []
lijstkleuren = []
rond = 0
nrond = 0
for x in range(len(fruitmand)):
    kleur = (fruitmand[x]['color'])
    if kleur not in lijstkleuren:
        lijstkleuren.append(kleur)
while loop == True:
    kleur = str(input("Kies e en kleur uit de kleuren : " + str(lijstkleuren)+"? "))
    if (kleur.lower()) not in lijstkleuren:
        print ("De Kleur " + kleur + " zit er niet in de fruitmand")
        loop = True
    else:
        print("Kleur zit in de lijst.")
        loop = False
for fruit in fruitmand:
            if fruit['color'] == kleur:
                if fruit['round'] == True:
                    rond += 1
                else:
                    nrond += 1
print (rond)
print (nrond)
verschil = rond - nrond
verschil = abs(verschil)
if rond > nrond:
    print (f"Er zijn {int(verschil)} meer ronde vruchten dan niet ronde vruchten in de kleur {str(kleur)}")
if rond < nrond:
        print (f"Er zijn {str(verschil)} minder ronde vruchten dan niet ronde vruchten in de kleur {str(kleur)}")
if rond == nrond:
    print (f"Er zijn {str(verschil)} ronde vruchten en {str(nrond)} niet ronde vruchten in de kleur {str(kleur)}")