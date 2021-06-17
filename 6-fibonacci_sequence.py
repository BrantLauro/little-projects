from time import sleep as sl

def din (text):
    for c in (text):
        print(c, end='', flush=True)
        sl(0.05)
    print()

def lin (qua,sym):
    print(qua*sym)

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

n = int(input('How many terms? '))
stop = 3
t1, t2 = 0, 1

if n < 1:
    print('Please enter a positive integer!')

if n == 1:
    print(t1)

if n > 1:
    print(f'{t1} → {t2}', end='')

while stop <= n:
    t = t1 + t2
    print(f' → {t}', end='')
    t1 = t2
    t2 = t
    stop += 1

print()
lin(40, "-=-")
