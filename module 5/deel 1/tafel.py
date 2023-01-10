import math
opnieuw= True
def getal(tafel:int):
    for x in range(11):
        antwoord=x*tafel
        print(x,"x",tafel,"=",antwoord)
while opnieuw == True:
    try:
        cijfer=int(input("Van welk getal wilt u de tafel zien? "))
        opnieuw=False
    except:
        print("dat is geen getal")
        continue
getal(cijfer)