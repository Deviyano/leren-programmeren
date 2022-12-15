from fruitmand import fruitmand
kleuren = []
for fruit in fruitmand:
    if fruit['name']=='druif':
        fruitmand.pop(fruitmand.index(fruit))
for i in range (len(fruitmand)):
    if fruitmand[i]['color'] not in kleuren:
        kleuren.append(fruitmand[i]['color'])
print (kleuren)