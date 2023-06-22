import random
from lingowords import*
from data import*
from termcolor import colored

def intro():
    print("Welkom bij Lingo!")

def random_woord():
    woord_letters=[]
    woord = random.choice(words)
    oud_goed.append(woord)
    for x in woord:
        woord_letters.append(x)
    return woord_letters

def raden(woord):
    letters=[]
    while True:
        if ronde["ronde"] == 1:
            print(woord[0]," _ _ _ _", end=" ")
            print("\n")
        gok = input("probeer het woord te raden: ").lower()
        if len(gok) >5 or len(gok) <5:
            print("Het woord moet 5 letters lang zijn")
            continue
        if gok.isalpha() == False:
            print("je mag alleen letters invoeren")
        
        else:
            for x in gok:
                letters.append(x)
                oud_woord.append(x)
            return letters
        
def check(gok, woord_letters):
    woord_kleuren=[]
    for x in range(5):
        if gok[x] == woord_letters[x]:
            woord_kleuren.append("green")
            oud_kleuren.append("green")
            continue 
        if gok[x] in woord_letters:
                if gok.count(gok[x]) > woord_letters.count(gok[x]):
                    woord_kleuren.append("red")
                    oud_kleuren.append("red")
                    continue
                else:
                    woord_kleuren.append("yellow")
                    oud_kleuren.append("yellow")
                    continue
                    
        else:
            woord_kleuren.append("red")
            oud_kleuren.append("red")
            continue
    return woord_kleuren

def einde(gok, woord,getal):
    if gok == woord:
        print("Goed gedaan je hebt het woord geraden!")
    else:
        print("Helaas je hebt het woord niet geraden het woord was",oud_goed[getal])
    
def opnieuw(gok):
    while True:
        opnieuw = input("Wil je nog een keer spelen? (ja/nee): ").lower()
        if opnieuw == "ja":
            gok.clear()
            if len(oud_woord) >= 5:
                oud_woord.clear()
                oud_kleuren.clear()
                ronde["ronde"] = 1
            return spel == True
        if opnieuw == "nee":
            print("Bedankt voor het spelen!")
            return spel == False
        else:
            print("Sorry dat snap ik niet")
            continue


def letters(gok,kleuren_plaats):
    plek=[]
    for x in range(len(kleuren_plaats)):
        if kleuren_plaats[x] == "green":
            plek.append(gok[x])
            continue
        else:
            plek.append("_")
            continue
    for x in plek:
        print(x, end=" ")
    print("\n")

def oud():
    getal=0
    for x in range(ronde["ronde"]-1):
        for x in range(5):
            print(colored(oud_woord[getal], oud_kleuren[getal],attrs=["bold","reverse"]), end=" ")
            getal+=1
        print("\n")