dag=input("welke dag is het vandaag")
ma="maandag"
di="dinsdag"
wo="woensdag"
do="donderdag"
vr="vrijdag"
za="zaterdag"
zo="zondag"
while dag == "maandag" or dag == "ma":
    print("di,wo,do,vr,za,zo")
    break
while dag == "dinsdag" or dag == "di":
    print("wo,do,vr,za,zo,ma")
    break
while dag == "woensdag" or dag == "wo":
    print("do,vr,za,zo,ma,di")
    break
while dag == "donderdag" or dag == "do":
    print("vr,za,zo,ma,di,wo")
    break
while dag == "vrijdag" or dag == "vr":
    print("za,zo,ma,di,wo,do")
    break
while dag == "zaterdag" or dag == "za":
    print("zo,ma,di,wo,do,vr")
    break
while dag == "zondag" or dag == "za":
    print("ma,di,wo,do,vr,za,")
    break