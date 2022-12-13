import random
ronde=1
gokken=0
gok=0
while ronde <=21:
    randoom= random.randint(1,1000)
    print(randoom)
    while gokken <=10:
        gokken=gokken+1
        gok=input("welk getal gokt u tussen 1 en 1000: ")
        if gok == "":
            gok=0
        try:
            gok = int(gok)
        except:
            continue
        totaal=abs(gok-randoom)
        if gok == randoom:
            print("geraden")
            gokken=gokken-10
            print("je score is ",ronde,"")
            volgende=input("Nog een getal raden? ja/nee: ").lower()
            if volgende=="ja":
                    ronde=ronde+1
                    break
            else: 
                volgende=="nee"
                print("u heeft gestopt goed gespeeld uw score is ",ronde,"")   
                quit()
        elif totaal <= 50 and totaal >20:
            print("je bent warm")
            if gok>=randoom:
                print("lager")
            if gok<=randoom:
                    print("hoger")            
        elif totaal <=20 and totaal >1:
             print("je bent heel warm")
             if gok>=randoom:
                print("lager")
             if gok<=randoom:
                print("hoger")
        else:
            if gok>=randoom:
                print("lager")
            if gok<=randoom:
                print("hoger")
    if gokken >= 10:
        print("je hebt al je 10 gokken gebruikt je score is ",ronde-1,"")
        quit()
    if ronde >= 21:
        print("je hebt alle ronde gehaalt dit is uw score ",ronde-1,"")
        quit()
    

    
