from fruitmand import fruitmand
lijst=[]
fruitmand.pop(4)
for x in range(len(fruitmand)):
    kleur=fruitmand[x]["color"]
    if kleur not in lijst:
        lijst.append(kleur)
print(lijst)
