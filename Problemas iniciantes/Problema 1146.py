x = 1
cont = 0

while(x != 0):
    x = int(input())

    for i in range(1, x+1):
        cont += 1
        if cont == x:
            print(i, end="\n")
            cont = 0
        else:
            print(i, end=" ")
