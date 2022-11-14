val = input().split()

x = int(val[0])
y = int(val[1])

cont = 0

for i in range(y):
    cont += 1
    if cont == x:
        print(i+1, end="\n")
        cont = 0
    else:
        print(i+1, end=" ")
