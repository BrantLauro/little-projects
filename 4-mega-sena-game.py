from time import sleep as sl
from random import randint as rd

def din (text):
    for c in (text):
        print(c, end='', flush=True)
        sl(0.05)

def lin (qua,sym):
    print(qua*sym)

game = []
correct_numbers = 0
guess = 0

for c in range(0, 6):
    number = rd(1,60)
    if number not in game:
        game.append(number)


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

din("Welcome to Lauro's Mega Sena - The Game \n"
    "The Pc made a Mega Sena game, and you have to guess it! \n")

for i in range(0, 6):
    while True:
        guess = int(input(f'Guess a number ({i+1}/6): [1/60] '))
        if guess > 60 or guess <= 0:
            din('Try Again! \n')
        else:
            break
    if guess in game:
        correct_numbers += 1

din(f"The genereted game was {game}! \n")
din(f"You hit {correct_numbers}/6 numbers of this game! \n")
