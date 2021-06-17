from random import randint as rd
from time import sleep as sl

def lin():
    print('='*30)

lin()
print(f"{'Mega-Sena':>19}")
lin()

games = []
times = int(input('How many games do you want to play? '))

for c in range(0, times):    
    games.append([])

    while len(games[c]) < 6:
        number = rd(1, 60)
        if number not in games[c]:
            games[c].append(number)

    games[c].sort()
    sl(0.1)
    print(games[c])

lin()
print(f"{'Good Luck':>19}")
lin()
