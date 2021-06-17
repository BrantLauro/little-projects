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
  ___      _     _                       _   _____                     
 / _ \  __| | __| |___    __ _ _ __   __| | | ____|_   _____ _ __  ___ 
| | | |/ _` |/ _` / __|  / _` | '_ \ / _` | |  _| \ \ / / _ \ '_ \/ __|
| |_| | (_| | (_| \__ \ | (_| | | | | (_| | | |___ \ V /  __/ | | \__ \ 
 \___/ \__,_|\__,_|___/  \__,_|_| |_|\__,_| |_____| \_/ \___|_| |_|___/
                                                                       
''')

din("Welcome to Lauro's Odds and Evens! \n"
    "You choose between Odd and Even, Then you enter a number, the pc randomize another... \n"
    "This numbers are sum, and if you was chosen thw right parity you wil")
