from ast import If
from logging.handlers import TimedRotatingFileHandler
import math
from multiprocessing.resource_sharer import stop
#Deviyano Acosta 
#990874836
#opdracht pizzacalculator
small=6,99
medium=9,99
large=12,99

keuze = input("Wilt u een small of medium of large pizza :")
aantal = input("hoeveel pizza's wilt u :")
elif aantal == "" :
    print("error")


elif keuze == "small":
    try: 
        prijs == str (aantal)*6,99
    except:
        print("dat is geen prijs")
        stop

elif keuze == "medium":
    try: 
        prijs == str (aantal)*9,99
    except:
        print("dat is geen prijs")
        stop
    
elif keuze =="large":
    try: 
     prijs== str (aantal)*12,99
    except:
        print("dat is geen prijs")
        stop


print(" ----------------------------")   
print("|uw totale bedrag is"+prijs+" |")
print(" ----------------------------") 

