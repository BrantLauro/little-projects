from time import sleep as sl
from random import randint as rd

def din (text):
    for c in (text):
        print(c, end='', flush=True)
        sl(0.05)
    print()

def lin (qua,sym):
    print(qua*sym)

print('''
 __  __                    ____                    
|  \/  | ___  __ _  __ _  / ___|  ___ _ __   __ _  
| |\/| |/ _ \/ _` |/ _` | \___ \ / _ \ '_ \ / _` |  
| |  | |  __/ (_| | (_| |  ___) |  __/ | | | (_| |   
|_|  |_|\___|\__, |\__,_| |____/ \___|_| |_|\__,_| 
             |___/                                                   
 _____ _              ____ 
|_   _| |__   ___    / ___| __ _ _ __ ___   ___ 
| | | | '_ \ / _ \  | |  _ / _` | '_ ` _ \ / _ \ 
| | | | | | |  __/  | |_| | (_| | | | | | |  __/
| |_| |_| |_|\___|   \____|\__,_|_| |_| |_|\___|

''')

din("Welcome to Lauro's Mega Sena - The Game! \n"
    "The Pc made a Mega Sena game, and you have to guess it!")

lin(30, '-=-')

game = []
correct_numbers = 0
guess = 0

for c in range(0, 6):
    number = rd(1,60)
    if number not in game:
        game.append(number)

for i in range(0, 6):
    while True:
        guess = int(input(f'Guess a number ({i+1}/6): [1/60] '))
        if guess > 60 or guess <= 0:
            din('Try Again!')
        else:
            break
    if guess in game:
        correct_numbers += 1

lin(30, "-=-")

din(f"The genereted game was {game}! \n"
    f"You hit {correct_numbers}/6 numbers of this game!")
