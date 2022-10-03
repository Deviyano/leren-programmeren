goed=True
punten=0
while goed==True : 
    vraag=input("?")
    if vraag=="quit":
        print(punten)
        goed=False
    else: 
        punten=punten+1
        goed=True


