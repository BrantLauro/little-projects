from time import sleep as sl
from random import randint as rd
from functions import din, lin 

print('''
 __  __                    ____                   
|  \/  | ___  __ _  __ _  / ___|  ___ _ __   __ _ 
| |\/| |/ _ \/ _` |/ _` | \___ \ / _ \ '_ \ / _` |
| |  | |  __/ (_| | (_| |  ___) |  __/ | | | (_| |
|_|  |_|\___|\__, |\__,_| |____/ \___|_| |_|\__,_|
             |___/                                
''')

din("Welcome to the Lauro's Mega Sena guesser! \n"
    "How many games do you want to play?")

games = []
times = int(input('Quantity: '))

lin(30, '-=-')

for counter in range(0, times):    
    games.append([])

    while len(games[counter]) < 6:
        number = rd(1, 60)
        if number not in games[counter]:
            games[counter].append(number)

    games[counter].sort()
    sl(0.1)
    print(games[counter])

lin(30, '-=-')

print('''
  ____                 _   _               _    _ 
 / ___| ___   ___   __| | | |   _   _  ___| | _| |
| |  _ / _ \ / _ \ / _` | | |  | | | |/ __| |/ / |
| |_| | (_) | (_) | (_| | | |__| |_| | (__|   <|_|
 \____|\___/ \___/ \__,_| |_____\__,_|\___|_|\_(_)
                                                  
''')
