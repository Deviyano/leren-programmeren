from importlib import import_module
import math

een_persoon_hele_dag=7.45
apersonen= input("met hoeveel personen bent u:")
personenaantal=int (apersonen)*7.45

vr_5min=0.37
amin=45
amin=input("voor hoeveel minuten wilt u de vr gebruiken: ")
vraantal= int (amin)*0.39
print(personenaantal+vraantal)
totaal_bedrag=72.30
totaal= int (apersonen)*(vraantal)+(personenaantal)

print("Dit geweldige dagje-uit met ",apersonen,"in de Speelhal met ",amin," kost je maar ",totaal," euro")