cijfers=[0,]
def reeks(aantal:int):
    totaal=0
    getal1=0
    getal2=1
    for x in range(aantal):
        totaal=getal1+getal2
        cijfers.append(totaal)
        getal2=(getal2-getal2)+getal1
        getal1=(getal1-getal1)+totaal
        totaal=0
    print(cijfers)
    return cijfers
reeks(11)