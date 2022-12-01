lijst = {}
repeat = True

while repeat == True:
    wat = input("Wat wil je nog aan je boodschappen lijst toevoegen? ").lower()
    try:
        aantal = int(input("Hoeveel wil je daarvan? "))
    except:
        continue
    if wat in lijst:
            lijst[wat] = lijst[wat] + aantal
    else:
            lijst[wat] = aantal

    herhalen = input("Wilt u nog meer toevoegen?").lower()

    if herhalen == "no" or herhalen == "nee":
        repeat = False


        print("Hier is jou lijst:")
        print("---------------------------")
        for key, value in lijst.items():
            print(value,"x ",key)
        print("---------------------------")