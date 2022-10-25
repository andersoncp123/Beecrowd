while True:
    lista = list()
    soma = 0
    ent = input().split()

    a = int(ent[0])
    b = int(ent[1])

    if a <= 0 or b <= 0:
        break

    else:
        lista.append(a)
        lista.append(b)
        lista.sort()

        for i in range(lista[0],lista[1]+1):
            soma += i

            print(i, end=" ")
        print("Sum={}". format(soma))
