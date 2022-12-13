cijfer = 50
som = str(cijfer)
totaal = cijfer
aantal = 0
while totaal <=1000:
    cijfer = cijfer +1
    totaal = totaal + cijfer
    som = som + "+" + str(cijfer)
    print(som + "+" + str(totaal))
    aantal = aantal+1
print ("",aantal,"sommen")