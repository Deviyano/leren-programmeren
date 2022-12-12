from fruitmand import fruitmand
lijst={}
for x in range(len(fruitmand)):
    lijst.update({fruitmand[x].get("weight")/1000: fruitmand[x].get("name")})
print(sorted(lijst.items(),reverse=True))