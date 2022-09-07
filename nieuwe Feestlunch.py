from importlib import import_module
import math

acroissantjes=17
croissantjes=0.39*acroissantjes

astokbrood=2
stokbrood=2.78*astokbrood

akorting=3
korting=0.50*akorting
print(croissantjes+stokbrood-korting)
totaal_bedrag=10.69
totaal=croissantjes+stokbrood-korting

print("De feestlunch kost je bij de bakker ",totaal," euro voor de ",croissantjes," en de ",stokbrood," als de ",korting," nog geldig zijn")
