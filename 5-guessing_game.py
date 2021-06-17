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

n = int(input('Your Guess: '))
r = rd(0, 100)
tries = 1

din('PROCESSING...')
lin(30, "-=-")

while n != r:
    if n > r:
        n = int(input(f'OH NO! You missed, The number is less! Try again: '))
        tries += 1
        din('PROCESSING...')
        lin(30, "-=-")
    elif n < r:
        n = int(input(f'OH NO! You missed, The number is better! Try again: '))
        tries += 1
        din('PROCESSING...')
        lin(30, "-=-")

if n == r:
    din('CONGRATULATIONS! You won!')
    din(f'With {tries} tries')
    lin(30, "-=-")
