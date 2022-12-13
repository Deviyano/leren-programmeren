from ast import If
from logging.handlers import TimedRotatingFileHandler
import math
from multiprocessing.resource_sharer import stop
#Deviyano Acosta 
#990874836
#opdracht pizzacalculator
small=6.99
medium=9.99
large=12.99

keuze = input("Wilt u een small of medium of large pizza :")
aantal = input("hoeveel pizza's wilt u :")
if aantal == "" :
    print("error")


if keuze == "small":
    try: 
        prijs = int (aantal)*6.99
    except:
        print("dat is geen prijs")
        stop

if keuze == "medium":
    try: 
        prijs = int (aantal)*9.99
    except:
        print("dat is geen prijs")
        stop
    
if keuze =="large":
    try: 
     prijs= int (aantal)*12.99
    except:
        print("dat is geen prijs")
        stop


print(" ----------------------------")   
print("|uw totale bedrag is",prijs," |")
print(" ----------------------------") 

