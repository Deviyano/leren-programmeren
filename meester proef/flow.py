from functions import *
from lingowords import *
from data import *
from time import sleep
getal=0

intro()

sleep(1)

while spel == True:

    woord=random_woord()

    for x in range(5):
        print(woord)

        gok=raden(woord)

        if gok == woord:
            break

        kleuren_plaats=check(gok, woord)

        ronde["ronde"]+=1

        oud()

        letters(gok, kleuren_plaats)
        
    einde(gok, woord,getal)

    getal+=1

    spel=opnieuw(gok)
