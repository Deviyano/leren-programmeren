import random
deck=["joker","joker"]
overig=[]
kleuren=["harten", "klaveren", "schoppen", "ruiten",]
kaarten=[" 2"," 3"," 4"," 5"," 6"," 7"," 8"," 9"," 10"," boer"," vrouw"," heer"," aas"]
for p in range(4):
    for x in range(13):
        combo = kleuren[p]+kaarten[x]
        deck.append(combo)
random.shuffle(deck)
for L in range(7):
    print("Kaart",L+1,deck.pop(L))
print("deck (47 kaarten): ",deck)