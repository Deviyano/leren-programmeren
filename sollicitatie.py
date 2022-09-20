print("-----------------------------------------------------")
print("Sollicitatie Circusdirecteur voor Circus HotelDeBotel")
print("hier komen de vragen")
print("-----------------------------------------------------")
naam = input ("wat is uw naam? ")
ervaring = input ("heeft u ervaring met dieren-jongleren of acrobatiek")
jaar = input ("Hoeveel jaar ervaring heeft u? ")
diploma = input ("heeft u een mbo diploma? ")
rijbewijs = input ("heeft u een rijbewijs? ") 
hoed = input ("bent u in bezit van een hoge hoed? ")
geslacht = input ("bent u een man of een vrouw? ")

if geslacht == "man" :
    haar = input ("hoelang is uw haar ")
if geslacht == "vrouw" :
    haar = input ("hoelang is uw haar ")      

lengte = input ("hoelang bent u?")
gewicht = input ("how zwaar bent u?")
certificaat = input ("heeft u het certificaat overleven met gevaarlijk personeel ")
randomvraag1 = input ("heeft u een clownsneus? ")
randomvraag2 = input ("heb je een broer of zus? ")
randomvraag3 = input ("wat was je vorige baan? ")
randomvraag4 = input ("heeft u huisdieren? ")

goed = False
if ervaring == "dieren" or "jongleren" or "acrobatiek" :
    if jaar == "5" or "4" or "3" :
        if rijbewijs == "ja" :
            if hoed == "ja" :
                if haar >= "10" or "20" :
                    if lengte >= "150" :
                        if gewicht >= "90" :
                            goed = True
                            if goed == True :
                             print ("gefeliciteerd ",naam," je bent geschikt voor deze baan.")

if goed == False:
    print ("sorry",naam," u bent niet geschikt voor deze baan") 
