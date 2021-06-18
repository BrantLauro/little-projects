from random import randint as rd
from functions import din, lin 

print('''
  ____                     _                ____                      
 / ___|_   _  ___  ___ ___(_)_ __   __ _   / ___| __ _ _ __ ___   ___ 
| |  _| | | |/ _ \/ __/ __| | '_ \ / _` | | |  _ / _` | '_ ` _ \ / _ \ 
| |_| | |_| |  __/\__ \__ \ | | | | (_| | | |_| | (_| | | | | | |  __/
 \____|\__,_|\___||___/___/_|_| |_|\__, |  \____|\__,_|_| |_| |_|\___|
                                   |___/                              

''')

din("Welcome to Lauro's Guessing Game! \n"
    "The Pc will think in a number between 0 and 100. Try to guess...")

lin(30, "-=-")

number = int(input('Your Guess: '))
pc_number = rd(0, 100)
tries = 1

din('PROCESSING...')

while number != pc_number:
    if number > pc_number:
        number = int(input(f'OH NO! You missed, The number is less! Try again: '))
        tries += 1
        din('PROCESSING...')
    elif number < pc_number:
        number = int(input(f'OH NO! You missed, The number is better! Try again: '))
        tries += 1
        din('PROCESSING...')

if number == pc_number:
    lin(30, "-=-")
    din('CONGRATULATIONS! You won!')
    din(f'With {tries} tries')
    
