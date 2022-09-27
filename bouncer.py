leeftijd=input ("Wat is uw leeftijd: ")
leeftijd=int(leeftijd)
if leeftijd >= 18 :
    print("welkom u mag naar binnen")
    if leeftijd >= 21 :
        naam=input ("wat is uw naam: ")
        print("hier heeft u een bandje om alcohol te halen")
        drink_keuze=input("Wat wilt u drinken bier of cola: ")
        if drink_keuze=="bier" :
            print("hier is een biertje dat wordt dan 1.50")
        if drink_keuze=="cola" :
            print("hier is uw cola dat wordt dan 1.00")
    else:
        naam=input ("wat is uw naam: ")
    if naam =="rudi" :
        print("u krijgt wel een sticker :) ")
    if naam =="Arnold" :
        print("u krijgt wel een sticker :) ")
    if naam =="jeroen" :
        print("u krijgt wel een sticker :) ")
    if naam =="kjeld" :
        print("u krijgt wel een sticker :) ") 
        cola=input("wilt u een cola")
        if cola=="ja":
            print("hier is uw gratis cola")
        if cola=="nee":
            print("ok dan niet")
        quit()
    else:
        print ("u mag naar binnen maar u krijgt geen bandje")
else:
    print("sorry u mag niet naar binnen")




