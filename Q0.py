import os
import time

GRAY = '\u001b[48;5;245m'
END = '\u001b[0m'

def Cadr(x):
    if x%2 == 0:
        print(f'{GRAY}{"  "*7}{END}')
        print(f'{GRAY}{"  "*1}{END}{"  "*5}{GRAY}{"  "*1}{END}')
        print(f'{GRAY}{"  "*1}{END}{"  "*5}{GRAY}{"  "*1}{END}')
        print(f'{GRAY}{"  "*1}{END}{"  "*5}{GRAY}{"  "*1}{END}')
        print(f'{GRAY}{"  "*1}{END}{"  "*5}{GRAY}{"  "*1}{END}')
        print(f'{GRAY}{"  "*7}{END}')
    if x%2 != 0:
        print(f'{END}{"  "*3}{GRAY}{"  "*1}{END}')
        print(f'{END}{"  "*2}{GRAY}{"  "*3}{END}')
        print(f'{END}{"  "*1}{GRAY}{"  "*2}{END}{"  "*1}{GRAY}{"  "*2}{END}')
        print(f'{GRAY}{"  "*2}{END}{"  "*3}{GRAY}{"  "*2}{END}')
        print(f'{END}{"  "*1}{GRAY}{"  "*2}{END}{"  "*1}{GRAY}{"  "*2}{END}')
        print(f'{END}{"  "*2}{GRAY}{"  "*3}{END}')
        print(f'{END}{"  "*3}{GRAY}{"  "*1}{END}')

for i in range (100):
    Cadr(i)
    time.sleep(0.5)
    os.system("cls") 