from random import randint as rd
from time import sleep as sl

def lin():
    print('='*30)

print('''
 __  __                    ____                   
|  \/  | ___  __ _  __ _  / ___|  ___ _ __   __ _ 
| |\/| |/ _ \/ _` |/ _` | \___ \ / _ \ '_ \ / _` |
| |  | |  __/ (_| | (_| |  ___) |  __/ | | | (_| |
|_|  |_|\___|\__, |\__,_| |____/ \___|_| |_|\__,_|
             |___/                                
''')

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
