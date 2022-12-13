from fruitmand import fruitmand
lijst=[]
fruitmand.pop({
    'name' : 'druif',
    'weight' : 5,
    'color' : 'red',
    'round' : True
})
for x in range(len(fruitmand)):
    kleur=fruitmand[x]["color"]
    if kleur not in lijst:
        lijst.append(kleur)
print(lijst)
