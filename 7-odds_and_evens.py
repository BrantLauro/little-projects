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
    "You choose between Odd and Even, Then you enter a number, the pc randomize another (1 to 10)... \n"
    "This numbers are sum, and if you was chosen the right parity you win!")
lin(30, "-=-")

number = counter = 0

while True:
    choose = ''
    pc = rd(1, 10)
    number = int(input('Type a number between 1 and 10: '))
    if 1 <= number <= 10:
        choose = input('Even or Odd? [E/O] ').strip().upper()[0]
        if choose == 'E':
            if (pc + number) % 2 == 0:
                din(f'Pc choose {pc}. {pc + number} is Even! You won congrats!')
                counter += 1
            else:
                din(f'Pc choose {pc}. {pc + number} is Odd! You lost, sorry!')
                break
        elif choose == 'O':
            if (pc + number) % 2 != 0:
                din(f'Pc choose {pc}. {pc + number} is Odd! You won congrats!')
                counter += 1
            else:
                din(f'Pc choose {pc}. {pc + number} is Even! You lost, sorry!')
                break
        else:
            din('[ERROR] Try Again!')
    else:
        din('Type a number between 1 and 10!')
lin(30, "-=-")
din(f'You won {counter} times!')
