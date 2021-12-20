import random

LIJSTT = ['Monopoly', 'Yathzee', 'Bridge', 'Poker', 'Pesten', 'Mens erger je niet' ,'Cluedo']
n = random.randint(1,10)
for x in range(-1, 6):
    x += 1
    print(LIJSTT[x],n)
    