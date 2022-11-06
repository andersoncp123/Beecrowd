x = 0
cont = 0
y = 0

while(x != 2):
    j = 0
    a = eval(input())

    if a < 0 or a > 10:
        print("nota invalida")
        x = 1

    elif a >= 0 and a <= 10:
        y += a
        cont += 1

    if cont == 2:
        print("media = {:.2f}". format(y/2))

        cont = 0
        y = 0
        
        print("novo calculo (1-sim 2-nao)")
        j = int(input())

        while(j < 1 or j > 2):
            print("novo calculo (1-sim 2-nao)")
            j = int(input())
        
        if j == 2:
            x = 2
