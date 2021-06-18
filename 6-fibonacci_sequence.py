from functions import din, lin 

print('''
 _____ _ _                                _ 
|  ___(_) |__   ___  _ __   __ _  ___ ___(_)
| |_  | | '_ \ / _ \| '_ \ / _` |/ __/ __| |
|  _| | | |_) | (_) | | | | (_| | (_| (__| |
|_|   |_|_.__/ \___/|_| |_|\__,_|\___\___|_|
                                            
 ____                                       
/ ___|  ___  __ _ _   _  ___ _ __   ___ ___ 
\___ \ / _ \/ _` | | | |/ _ \ '_ \ / __/ _ \ 
 ___) |  __/ (_| | |_| |  __/ | | | (_|  __/
|____/ \___|\__, |\__,_|\___|_| |_|\___\___|
               |_|                          

''')

din("Welcome to Lauro's Fibonacci Sequence! \n"
    "The Pc can show how many terms of the Fibonacci Sequence you want!")
lin(40, "-=-")

number_terms = int(input('How many terms? '))
stop = 3
term1, term2 = 0, 1

if number_terms < 1:
    print('Please enter a positive integer!')

if number_terms == 1:
    print(term1)

if number_terms > 1:
    print(f'{term1} → {term2}', end='')

while stop <= number_terms:
    term = term1 + term2
    print(f' → {term}', end='')
    term1 = term2
    term2 = term
    stop += 1

print()
lin(40, "-=-")
