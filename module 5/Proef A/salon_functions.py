from salon_data import *
def intro():
    print("Welkom bij Papi Gelato")

def bolletjes(klant:str):
    no_bol=True
    if klant == "zakelijk":
        while no_bol==True:
                try:
                    aantal_liter=int(input("Hoeveel liter aan ijs wilt u?: "))
                except:
                    print("Sorry dat snap ik niet...")
                    continue 
                if aantal_liter <= 0:
                    print("Sorry dat snap ik niet...")
                    continue
                else:
                    return aantal_liter
    else:
        while no_bol==True:
            try:
                aantal=int(input("Hoeveel bolletjes wilt u?: "))
            except:
                print("Sorry dat snap ik niet...")
                continue

            if aantal >= 1 and aantal <= 3:
                no_bol=False
                return aantal
            if aantal >= 4 and aantal <=8: 
                no_bol=False
                return aantal
            if aantal >= 8:
                print("Sorry, zulke grotebakken hebben we niet")
                continue

            else:
                print("Sorry dat snap ik niet...")
                continue    

def verpakking(aantal:int):
    no_verpakking=True
    while no_verpakking==True:
        if aantal >= 1 and aantal <= 3:
            keuze=input("Wilt u deze in een hoorntje of een bakje?: ").lower()
            if keuze == "hoorntje":
                return keuze
            if keuze == "bakje":
                return keuze
            else:
                print("Sorry dat snap ik niet...")
                continue      
        else:
            return "bakje"

def meer_bestellen():
    opnieuw=True
    while opnieuw==True:
        meer=input("Wilt u nog meer bestellen? (ja/nee): ")
        if meer == "ja":
            return True
        if meer == "nee":
            return False
        else:
            print("Sorry dat snap ik niet...")

def hier_is_uw_ijsje(aantal:int,keuze:str):
    print("Hier is uw ",keuze," met",aantal,"bolletje(s).")

def totaalprijs(keuze,aantal,topping_keuze):
    totalenprijzen["prijsbol"]=aantal*prijzen["Bollentjes"]
    totalenprijzen["prijshoorn"]=aantalen["Horentjes"]*prijzen["Horentjes"]
    totalenprijzen["prijsbak"]=aantalen["Bakjes"]*prijzen["Bakjes"]
    totaal_toppings["Slagroom"]=aantal_toppings["Slagroom"]*prijzen["Slagroom"]
    if aantal_toppings["Sprinkels"] >= 1:
        totaal_toppings["Sprinkels"]=totaal_toppings["Sprinkels"]+aantal*prijzen["Sprinkels"]
    totaal_toppings["Caramel"]=aantal_toppings["Caramel"]*prijzen["Caramel"]
    if keuze == "bakje" and topping_keuze == "Caramel":
            totaal_toppings["Caramel"]= totaal_toppings["Caramel"]+0.30
    totalenprijzen["prijstopping"]=totaal_toppings["Slagroom"]+totaal_toppings["Sprinkels"]+totaal_toppings["Caramel"]
    totaal_smaken["Aardbei"]=smaken["Aardbei"]*prijzen["Bollentjes"]
    totaal_smaken["Chocolade"]=smaken["Chocolade"]*prijzen["Bollentjes"]
    totaal_smaken["Munt"]=smaken["Munt"]*prijzen["Bollentjes"]
    totaal_smaken["Vanille"]=smaken["Vanille"]*prijzen["Bollentjes"]

    
def bon(totalenprijzen, klant:str):
    print("---------[papi gelato]---------")
    if klant == "zakelijk":
        if smaken["Aardbei"] >=1:
            print("L.Aardbei:       ",smaken["Aardbei"],"X","{:,.2f}".format(prijzen["liter"]),"=","{:,.2f}".format(totaal_smaken["Aardbei"]))
        if smaken["Chocolade"] >=1:
            print("L.Chocolade:     ",smaken["Chocolade"],"X","{:,.2f}".format(prijzen["liter"]),"=","{:,.2f}".format(totaal_smaken["Chocolade"]))
        if smaken["Munt"] >=1:
            print("L.Munt:          ",smaken["Munt"],"X","{:,.2f}".format(prijzen["liter"]),"=","{:,.2f}".format(totaal_smaken["Munt"]))
        if smaken["Vanille"] >=1:
            print("L.Vanille:       ",smaken["Vanille"],"X","{:,.2f}".format(prijzen["liter"]),"=","{:,.2f}".format(totaal_smaken["Vanille"]))
    else:
        if smaken["Aardbei"] >=1:
            print("B.Aardbei:       ",smaken["Aardbei"],"X","{:,.2f}".format(prijzen["Bollentjes"]),"=","{:,.2f}".format(totaal_smaken["Aardbei"]))
        if smaken["Chocolade"] >=1:
            print("B.Chocolade:     ",smaken["Chocolade"],"X","{:,.2f}".format(prijzen["Bollentjes"]),"=","{:,.2f}".format(totaal_smaken["Chocolade"]))
        if smaken["Munt"] >=1:
            print("B.Munt:          ",smaken["Munt"],"X","{:,.2f}".format(prijzen["Bollentjes"]),"=","{:,.2f}".format(totaal_smaken["Munt"]))
        if smaken["Vanille"] >=1:
            print("B.Vanille:       ",smaken["Vanille"],"X","{:,.2f}".format(prijzen["Bollentjes"]),"=","{:,.2f}".format(totaal_smaken["Vanille"]))
        if aantalen["Horentjes"] >=1:
            print("Horrentjes:     ",aantalen["Horentjes"],"X","{:,.2f}".format(prijzen["Horentjes"]),"=","{:,.2f}".format(totalenprijzen["prijshoorn"]))
        if aantalen["Bakjes"] >=1:
            print("Bakjes:        ",aantalen["Bakjes"],"X","{:,.2f}".format(prijzen["Bakjes"]),"=","{:,.2f}".format(totalenprijzen["prijsbak"]))
        if aantal_toppings["Slagroom"] >=1 or aantal_toppings["Sprinkels"] >=1 or aantal_toppings["Caramel"] >=1:
                print("Toppings:                =" ,"{:,.2f}".format(totalenprijzen["prijstopping"]))
    print("               --------------- +")
    print("Totaal:                 ","{:,.2f}".format(totalenprijzen["totaal"]))
    print("-------------------------------")

def smaak(aantal:int,klant:str):
    opnieuw=True
    for x in range(1,aantal+1):
        while opnieuw==True:
            if klant == "particulier":
                smaak_keuze=input("Welke smaak wilt u voor bolletje nummer "+str(x)+" ? A) Aardbei, C) Chocolade, M) Munt of V) Vanille?:  ").lower()
            if klant == "zakelijk":
                smaak_keuze=input("Welke smaak wilt u voor liter nummer "+str(x)+" ? A) Aardbei, C) Chocolade, M) Munt of V) Vanille?:  ").lower()
            if smaak_keuze == "a":
                smaken["Aardbei"]=smaken["Aardbei"]+1
                break

            if smaak_keuze == "c":
                smaken["Chocolade"]=smaken["Chocolade"]+1
                break

            if smaak_keuze == "m":
                smaken["Munt"]=smaken["Munt"]+1
                break

            if smaak_keuze == "v":
                smaken["Vanille"]=smaken["Vanille"]+1
                break

            else:
                print("Sorry dat snap ik niet...")
                continue

def toppings():
    opnieuw=True
    while opnieuw == True:
        topping_keuze=input("Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus?: ").lower()
        if topping_keuze == "a":
            break
        if topping_keuze == "b":
            aantal_toppings["Slagroom"]=aantal_toppings["Slagroom"]+1
            return "Slagroom"
        if topping_keuze == "c":
            aantal_toppings["Sprinkels"]=aantal_toppings["Sprinkels"]+1
            return "Sprinkels"
        if topping_keuze == "d":
            aantal_toppings["Caramel"]=aantal_toppings["Caramel"]+1
            return "Caramel"
        else:
            print("Sorry dat snap ik niet...")
            continue
def de_klant():
    while True:
        klant=input("Bent u 1) een particuliere klant of 2) een zakelijke klant?: ")
        if klant == "1":

            return "particulier"
        
        if klant == "2":
            return "zakelijk"
        
        else:
            print("Sorry dat snap ik niet...")
            continue

def liter_berekenen():
    totaal_smaken["Aardbei"]=prijzen["liter"]*smaken["Aardbei"]
    totaal_smaken["Chocolade"]=prijzen["liter"]*smaken["Chocolade"]
    totaal_smaken["Munt"]=prijzen["liter"]*smaken["Munt"]
    totaal_smaken["Vanille"]=prijzen["liter"]*smaken["Vanille"]
    totalenprijzen["totaal"]=totaal_smaken["Aardbei"]+totaal_smaken["Chocolade"]+totaal_smaken["Munt"]+totaal_smaken["Vanille"]
