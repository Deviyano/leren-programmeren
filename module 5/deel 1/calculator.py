def calculator():
    vragen=True
    getal1=0
    aantal=0
    while vragen == True:
        try:
            totaal=float(input("welk getal wilt u gebruiken? "))
            vragen=False
        except:
            print("Sorry dat is geen getal")
    firstround=False
    delen0=True
    while firstround == False:
        print("wat wilt u doen?")
        print("A) optellen")
        print("B) aftrekken")
        print("C) delen")
        print("D) vermenigvuldigen")
        print("E) ophogen")
        print("F) verlagen")
        print("G) halfveren")
        print("H) verdubbelen")
        print("I) Niets")
        choice=input("kies: ").capitalize()
        if choice =="A":
            vragen=True
            print("Getallen optellen")
            while vragen == True:
                try:
                    getal2=float(input("Met Welk getal wilt u optellen? "))
                except:
                    print("Sorry dat is geen getal")
                    continue
                vragen=False
                getal1=(getal1-getal1)+totaal
                totaal=totaal+getal2
                print(getal1,"+",getal2 ,"=", totaal)
                aantal=aantal+1
                continue
        if choice == "B":
            vragen=True
            print("Getallen aftrekken")
            while vragen == True:
                try:
                    getal2=float(input("Met Welk getal wilt u aftrekken? "))
                except:
                    print("Sorry dat is geen getal")
                    continue
                vragen=False
                getal1=(getal1-getal1)+totaal
                totaal=totaal-getal2
                print(getal1,"-",getal2 ,"=", totaal)
                aantal=aantal+1
                continue
        if choice == "C":
            delen0=True
            print("Getallen delen")
            while delen0 == True:
                try:
                    getal2=float(input("Met Welk getal wilt u delen? "))
                except:
                    print("Sorry dat is geen getal")
                    continue
                if getal2 == int("0"):
                    print("Sorry u kunt niet delen door 0")
                    continue
                else:
                    delen0=False
                    getal1=(getal1-getal1)+totaal
                    totaal=totaal/getal2
                    print(getal1,":",getal2 ,"=", totaal)
                    aantal=aantal+1
                    continue
        if choice == "D":
            vragen=True
            print("Getallen vermenigvuldigen")
            while vragen == True:
                try:
                    getal2=float(input("Met Welk getal wilt u vermenigvuldigen? "))
                except:
                    print("Sorry dat is geen getal")
                    continue
                vragen=False
                getal1=(getal1-getal1)+totaal
                totaal=totaal*getal2
                print(getal1,"X",getal2 ,"=", totaal)
                aantal=aantal+1
                continue
        if choice == "E":
            print("Getallen ophogen")
            getal1=(getal1-getal1)+totaal
            totaal=totaal+1
            print(getal1,"+ 1 =",totaal)
            aantal=aantal+1
            continue
        if choice == "F":
            print("Getallen verlagen")
            getal1=(getal1-getal1)+totaal
            totaal=totaal-1
            print(getal1,"- 1 =",totaal)
            aantal=aantal+1
            continue
        if choice == "G":
            print("Getallen halfveren")
            getal1=(getal1-getal1)+totaal
            totaal=totaal/2
            print(getal1,": 2 =",totaal)
            aantal=aantal+1
            continue
        if choice == "H":
            print("Getallen verdubbelen")
            getal1=(getal1-getal1)+totaal
            totaal=totaal*2
            print(getal1,"X 2 =",totaal)
            aantal=aantal+1
            continue
        if choice =="I":
            if aantal<=0:
                print("U moet nog een berekening maken")
                continue
            if aantal>=0:
                firstround=True
                print("Uw laatste antwoord was ",totaal,)
        else:
            print("sorry dat is geen optie")
            continue
calculator()