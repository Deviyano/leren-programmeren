from importlib import import_module
import math

acroissantjes= input("hoeveel croissanten wilt u:")
croissantjes= int (acroissantjes)*0.39

astokbrood=input("hoeveel stokbroden wilt u:")
stokbrood= int (astokbrood) * 2.78

akorting=input("hoeveel korting bonnen heeft u:")
korting= int (akorting)*0.50
print(croissantjes+stokbrood-korting)
totaal_bedrag=10.69
totaal=croissantjes+stokbrood-korting

print("De feestlunch kost je bij de bakker ",totaal," euro voor de ",croissantjes," en de ",stokbrood," als de ",korting," nog geldig zijn")

