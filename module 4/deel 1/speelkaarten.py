import random
deck=["joker","joker"]
kleuren=["harten", "klaveren", "schoppen", "ruiten",]
kaarten=["2","3","4","5","6","7","8","9","10","boer","vrouw","heer","aas"]
for p in range(len(kleuren)):
    for x in range(len(kaarten)):
        combo = kleuren[p]+" "+kaarten[x]
        deck.append(combo)
random.shuffle(deck)
for L in range(7):
    print("Kaart",L+1,deck.pop(L))
print("deck",len(deck),"kaarten: ",deck)