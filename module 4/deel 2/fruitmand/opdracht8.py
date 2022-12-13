from fruitmand import fruitmand
totaal=0
fruitmand.append({
    'name' : 'watermelon',
    'weight' : 3500,
    'color' : 'groen',
    'round' : True})
for x in range(len(fruitmand)):
    gewicht=fruitmand[x]["weight"]
    totaal=totaal+gewicht
print(totaal)

