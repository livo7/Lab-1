RED = '\u001b[41m'
BLUE = '\u001b[44m'
END = '\u001b[0m'

File = open("sequence.txt")
Data = File.readlines()
Count = 0
for i in range(len(Data)):
    if "-" in Data[i]:
        Count += 1
print(f'Чисел больше 0: {BLUE}{" " * (len(Data) - Count)}{END}{(len(Data) - Count) / len(Data) * 100}%')
print(f'Чисел меньше 0: {RED}{" " * Count}{END}{Count / len(Data) * 100}%')