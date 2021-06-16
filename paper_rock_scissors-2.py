from time import sleep as sl
from random import randint as rd

def din (text):
    for c in (text):
        print(c, end='', flush=True)
        sl(0.05)

def lin (qua,sym):
    print(qua*sym)

print('''
 ____                         ____            _                      _ 
|  _ \ __ _ _ __   ___ _ __  |  _ \ ___   ___| | __   __ _ _ __   __| |
| |_) / _` | '_ \ / _ \ '__| | |_) / _ \ / __| |/ /  / _` | '_ \ / _` |
|  __/ (_| | |_) |  __/ |    |  _ < (_) | (__|   <  | (_| | | | | (_| |
|_|   \__,_| .__/ \___|_|    |_| \_\___/ \___|_|\_\  \__,_|_| |_|\__,_|
           |_|                                                         
 ____       _                    
/ ___|  ___(_)___ ___  ___  _ __ 
\___ \ / __| / __/ __|/ _ \| '__|
 ___) | (__| \__ \__ \ (_) | |   
|____/ \___|_|___/___/\___/|_|   
''')

din("Welcome to the Lauro's Paper Rock and Scissor \n")
din('Paper Rock or Scissor? \n')
while True:
    p1_choice = 0
    while p1_choice not in [1, 2 , 3]:
        p1_choice = int(input('[1] Paper \n'
                              '[2] Rock \n'
                              '[3] Scissor '))
        lin(30, '~')
        p2_choice = rd(1, 3)
    if p1_choice == 1 and p2_choice == 2 or p1_choice == 2 and p2_choice == 3 or p1_choice == 3 and p2_choice == 1:
        print('You Win!')
        continue_choice = ' '
        while continue_choice not in 'NY':
            continue_choice = input('Do you want to play again? [Y/N]').upper().strip()[0]
            lin(30, '~')
        if continue_choice == 'N':
            break
    if p2_choice == 1 and p1_choice == 2 or p2_choice == 2 and p1_choice == 3 or p2_choice == 3 and p1_choice == 1:
        print('You Lose!')
        continue_choice = ' '
        while continue_choice not in 'NY':
            continue_choice = input('Do you want to play again? [Y/N]').upper().strip()[0]
            lin(30, '~')
        if continue_choice == 'N':
            break
    if p1_choice == p2_choice:
        print('Tied!')
        lin(30, '~')
