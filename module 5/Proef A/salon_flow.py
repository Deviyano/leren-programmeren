from salon_functions import *
from salon_data import *
from time import sleep
door_bestellen=True
intro()
sleep(2)
klant=de_klant()
while door_bestellen==True:

    aantal=bolletjes(klant)

    aantalen["Bollentjes"] = aantalen["Bollentjes"]+aantal

    smaak(aantal,klant)
    if klant == "particulier":

        keuze=verpakking(aantal)

        if keuze == "hoorntje":  
            aantalen["Horentjes"] = aantalen["Horentjes"]+1
        else:
            aantalen["Bakjes"] = aantalen["Bakjes"]+1

        topping_keuze=toppings()

        hier_is_uw_ijsje(aantal,keuze)

        door_bestellen=meer_bestellen()

        if keuze == "bakje" and topping_keuze == "Caramel":
            totaal_toppings["Cbakje"]=totaal_toppings["Cbakje"]+0.30

        totaalprijs(keuze,aantal,topping_keuze)

    else:
        liter_berekenen()
        break

if klant == "particulier":
    totalenprijzen["prijstopping"]=totaal_toppings["Slagroom"]+totaal_toppings["Sprinkels"]+totaal_toppings["Caramel"]+totaal_toppings["Cbakje"]
    totalenprijzen["totaal"]=totaal_smaken["Aardbei"]+totaal_smaken["Chocolade"]+totaal_smaken["Vanille"]+totalenprijzen["prijshoorn"]+totalenprijzen["prijsbak"]+totalenprijzen["prijstopping"]
bon(totalenprijzen,klant)


print(totaal_toppings["Slagroom"])
print(totaal_toppings["Sprinkels"])
print(totaal_toppings["Caramel"])
print(totaal_toppings["Cbakje"])
print(totalenprijzen["prijstopping"])