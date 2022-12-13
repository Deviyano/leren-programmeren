import random
overig=["joker","joker"]
deck=[]
kleuren=["harten", "klaveren", "schoppen", "ruiten",]
kaarten=["2","3","4","5","6","7","8","9","10","een boer","een vrouw","een heer","een aas"]
for x in range(13):
    overig.append(kleuren[0]),overig.append(kaarten[x])
    overig.append(kleuren[1]),overig.append(kaarten[x])
    overig.append(kleuren[2]),overig.append(kaarten[x])
    overig.append(kleuren[3]),overig.append(kaarten[x])
random.shuffle(overig)
deck.append(overig[0])
deck.append(overig[1])
deck.append(overig[2])
deck.append(overig[3])
deck.append(overig[4])
deck.append(overig[5])
deck.append(overig[6])
print(deck)
print(overig)