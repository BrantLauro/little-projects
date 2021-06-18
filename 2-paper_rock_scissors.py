from random import randint as rd
from functions import din, lin 

print('''
 ____            _      ____                       
|  _ \ ___   ___| | __ |  _ \ __ _ _ __   ___ _ __ 
| |_) / _ \ / __| |/ / | |_) / _` | '_ \ / _ \ '__|
|  _ < (_) | (__|   <  |  __/ (_| | |_) |  __/ |   
|_| \_\___/ \___|_|\_\ |_|   \__,_| .__/ \___|_|   
                                  |_|              
 ____       _                        
/ ___|  ___(_)___ ___  ___  _ __ ___ 
\___ \ / __| / __/ __|/ _ \| '__/ __|
 ___) | (__| \__ \__ \ (_) | |  \__ \ 
|____/ \___|_|___/___/\___/|_|  |___/ 
''')

din("Welcome to the Lauro's Rock Paper Scissors! \n"
    "Rock Paper or Scissor?")

lin(30, '-=-')

while True:
    p1_choice = 0
    while p1_choice not in [1, 2 , 3]:
        p1_choice = int(input('[1] Rock \n'
                              '[2] Paper \n'
                              '[3] Scissor '))

        lin(30, '-=-')
        p2_choice = rd(1, 3)

    if p1_choice == 1 and p2_choice == 3 or p1_choice == 2 and p2_choice == 1 or p1_choice == 3 and p2_choice == 2:
        din('You Win!')
        continue_choice = ' '

        while continue_choice not in 'NY':
            continue_choice = input('Do you want to play again? [Y/N] ').upper().strip()[0]
        if continue_choice == 'N':
            break

    if p2_choice == 1 and p1_choice == 3 or p2_choice == 2 and p1_choice == 1 or p2_choice == 3 and p1_choice == 2:
        din('You Lose!')
        continue_choice = ' '
        
        while continue_choice not in 'NY':
            continue_choice = input('Do you want to play again? [Y/N] ').upper().strip()[0]
        if continue_choice == 'N':
            break

    if p1_choice == p2_choice:
        din('Tied!')
