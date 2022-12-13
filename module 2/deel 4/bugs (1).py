import random

name = input('Wat is jouw naam? ')
print('Hallo', name)

favoriteSeason = input("'Wat is jouw favorite seizoen "+ name + "? A) Lente, B) Zomer, C) Herfst of D) Winter '")
answer = favoriteSeason
print(answer)
if answer == "A" :
    print("Ik hou ook van de lente!")
elif answer == 'B':
    print("De zomer is voor mij te warm.")
elif answer == 'C':
    print("Mooi he, al die blaadjes die dan van de boom vallen.")
elif answer == 'D':
    print("Is de winter niet erg koud?")
else:
    print("Die ken ik niet...")

favoriteColor = input('En wat is je favoriete kleur? ') 
trueOrFalse = str(random.randint(0,1))
if favoriteColor:
    print('Ik vind dat ook een mooie kleur!')
elif True or False :
    print("'TBH, ik hou niet zo van {}...'.format"""+ favoriteColor +"")
    
num1 = random.randint(1,10) 
num2 = random.randint(5,15)

try:
    number = int (input("En weet jij wat "+ str(num1)+"+"+str(num2)+" is? "))
    if int(number == (num1)+(num2)):
        print('Dat is juist')
    else:
        print("Nee dat klopt niet {}.format "+ name +"")
except:
    print('Dat is geen nummer!')
