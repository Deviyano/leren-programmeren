def naam():
    dict={}
    opnieuw= True
    while opnieuw == True:
        name =input("Wat is de naam van de persoon? ")
        if name != "stop":
            while True:
                try:
                    leeftijd = int(input("Hoe oud is de persoon? "))
                    dict[name] = leeftijd
                    break
                except:
                    if  leeftijd != "stop":
                        print("Dat is geen getal")
                        continue
                    else:
                        return dict
        else: 
            return dict
for key,values in dict.items(naam()):
    print(key, "is", values, "jaar oud")