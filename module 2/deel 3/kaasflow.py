from ast import If

gelekaas = input("Is de kaas geel? ")
if gelekaas == "ja" :
    gatenkaas = input("Zitten er gaten in? ")
    if gatenkaas == "ja" :
        durekaas = input("Is de kaas belagelijk duur? ")
        if  durekaas=="ja" :
            print("Emmenthaler")
        elif durekaas=="nee" : 
            print("Leerdammer")  
    elif gatenkaas =="nee" :
        hardekaas = input("Is de kaas zo hard als een steen?")
        if hardekaas =="ja" :
            print("Parmigiano Reggiano")
        elif hardekaas =="nee" :
            print("Goudse Kaas")
elif gelekaas =="nee" :
    schimmelkaas = input("Heeft de kaas blauwe schimmel? ")
    if schimmelkaas =="ja" :
        korstkaas = input ("Heeft de kaas een korst? ")
        if korstkaas =="ja" :
            print("Blue de Rochbaron")
        elif korstkaas == "nee" :
            print("Foume d'Ambert")
    elif schimmelkaas =="nee" :
        schimmelkaaszonderschimmel = input("Heeft de kaas een korst?")
        if schimmelkaaszonderschimmel =="ja" :
            print("Camembert")
        elif schimmelkaaszonderschimmel =="nee" :
            print("Mozzarella")