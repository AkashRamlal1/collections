import random
print('hoeveel M&Ms wil je hebben ')
aantal = int(input('kies je aantal'))
kleur = ['oranje','blauw','groen','bruin']
Zak = {}
def snoepjes(aantal):
    for i in range(aantal):
        wilkleur = random.choice(kleur)
        if wilkleur in Zak:
            
            Zak[wilkleur] += 1
        else:
            Zak.update({wilkleur : 1})

    return Zak
print(sorted(snoepjes(aantal).items(), key=lambda kv: kv[1], reverse=True))    


