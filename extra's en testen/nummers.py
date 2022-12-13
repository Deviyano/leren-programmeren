lijst=[]
for x in range(20):
    try:
        vraag=int(input("kies een getal: "))
        lijst.append(vraag)
    except:
        continue
lijst.sort()
delen = list(filter(lambda x: (x % 3 == 0), lijst))
print("het kleinste getal is",lijst[0])
print("het grootste getal is",lijst[-1])
print("er zijn",len(delen),"getallen deelbaar door 3")
