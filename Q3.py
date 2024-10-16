zn=[[0, 0] for a in range(10)]

for i in range (0, 10):
    y=i**2
    zn[i]=[i, y]
for i in range(1, 10):
    if zn[-i][1]<10:
        zn[-i][1]=" "+str(zn[-i][1])
    print(zn[-i][1], end="")
    print(f'{" "*(zn[-i][0]-1)}', "*", sep="")
print("  ", end="")
for i in range (1, 10):
    print(zn[i][0], sep='', end='')