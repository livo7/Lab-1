RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
END = '\u001b[0m'

for i in range (0, 4):
    for y in range (0, 3):
        if y==0:
            print(f'{BLUE}{"  "*4}{END}', end="")
        if y==1:
            print(f'{WHITE}{"  "*4}{END}', end="")
        if y==2:
            print(f'{RED}{"  "*4}{END}')