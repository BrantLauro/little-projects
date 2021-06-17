from time import sleep as sl

def din (text):
    for c in (text):
        print(c, end='', flush=True)
        sl(0.01)
    print()

def lin (qua,sym):
    print(qua*sym)

din('''
 _   _      _ _        __        __         _     _ _ 
| | | | ___| | | ___   \ \      / /__  _ __| | __| | |
| |_| |/ _ \ | |/ _ \   \ \ /\ / / _ \| '__| |/ _` | |
|  _  |  __/ | | (_) |   \ V  V / (_) | |  | | (_| |_|
|_| |_|\___|_|_|\___/     \_/\_/ \___/|_|  |_|\__,_(_)
''')

din("Welcome to Lauro's Hello World! \n"
    "Thanks for playing this program. I Lov U!")

lin(50, '~')
