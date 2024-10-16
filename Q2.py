WHITE= '\u001b[47m'
END= '\u001b[0m'

print("введите чиcло повторений от 1 до 3","k=...", sep="\n")
k=int(input())
if k>3:
    print("error")
    breakpoint
if k ==1:
    print(f'{WHITE}{"  "*5}{END}')
    print(f'{WHITE}{"  "}{END}{"  "}{WHITE}{"  "}{END}{"  "}{WHITE}{"  "}{END}')
if k ==2:
    print(f'{WHITE}{"  "*9}{END}')
    print(f'{WHITE}{"  "}{END}{"  "}{WHITE}{"  "}{END}{"  "}{WHITE}{"  "}{END}{"  "}{WHITE}{"  "}{END}{"  "}{WHITE}{"  "}{END}')
if k ==3:
    print(f'{WHITE}{"  "*13}{END}')
    print(f'{WHITE}{"  "}{END}{"  "}{WHITE}{"  "}{END}{"  "}{WHITE}{"  "}{END}{"  "}{WHITE}{"  "}{END}{"  "}{WHITE}{"  "}{END}{"  "}{WHITE}{"  "}{END}{"  "}{WHITE}{"  "}{END}')

if k ==1:
    print(f'{WHITE}{"  "}{WHITE}{"  "}{END}{"  "}{WHITE}{"  "}{WHITE}{"  "}{END}')
if k ==2:
    print(f'{WHITE}{"  "}{WHITE}{"  "}{END}{"  "}{WHITE}{"  "}{WHITE}{"  "}{WHITE}{"  "}{END}{"  "}{WHITE}{"  "}{WHITE}{"  "}{END}')
if k ==3:
    print(f'{WHITE}{"  "}{WHITE}{"  "}{END}{"  "}{WHITE}{"  "}{WHITE}{"  "}{WHITE}{"  "}{END}{"  "}{WHITE}{"  "}{WHITE}{"  "}{WHITE}{"  "}{END}{"  "}{WHITE}{"  "}{WHITE}{"  "}{END}')
if k ==1:
    print(f'{WHITE}{"  "}{END}{"  "}{WHITE}{"  "}{END}{"  "}{WHITE}{"  "}{END}')
    print(f'{WHITE}{"  "*5}{END}')
if k ==2:
    print(f'{WHITE}{"  "}{END}{"  "}{WHITE}{"  "}{END}{"  "}{WHITE}{"  "}{END}{"  "}{WHITE}{"  "}{END}{"  "}{WHITE}{"  "}{END}')
    print(f'{WHITE}{"  "*9}{END}')
if k ==3:
    print(f'{WHITE}{"  "}{END}{"  "}{WHITE}{"  "}{END}{"  "}{WHITE}{"  "}{END}{"  "}{WHITE}{"  "}{END}{"  "}{WHITE}{"  "}{END}{"  "}{WHITE}{"  "}{END}{"  "}{WHITE}{"  "}{END}')
    print(f'{WHITE}{"  "*13}{END}')