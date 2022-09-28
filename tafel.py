import math

getal= input ("welk getal wilt u gebruiken: ")
getal= int(getal)

for x in range(1,11):
    print(x, *"X",getal,"=",x*getal)
