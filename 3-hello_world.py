from time import sleep as sl

def din (text):
    for c in (text):
        print(c, end='', flush=True)
        sl(0.01)

din('''
▌ ▌   ▜▜     ▌ ▌      ▜   ▌▐ 
▙▄▌▞▀▖▐▐ ▞▀▖ ▌▖▌▞▀▖▙▀▖▐ ▞▀▌▐ 
▌ ▌▛▀ ▐▐ ▌ ▌ ▙▚▌▌ ▌▌  ▐ ▌ ▌▝ 
▘ ▘▝▀▘ ▘▘▝▀  ▘ ▘▝▀ ▘   ▘▝▀▘▝ 
''')