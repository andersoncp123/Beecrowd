casos = 1
while True:
    try:
        numero = 1
        ent = int(input())

        for i in range(ent + 1):
            numero += i

        if numero == 1:
            print("Caso {}: {} numero".format(casos,numero))
        else:
            print("Caso {}: {} numeros".format(casos,numero))

        if ent == 0:
            print(0)
        else:
            print(0, end=" ")

        for i in range(ent + 1):
            for j in range(i):
                if i == ent and j == ent - 1:
                    print(i)
                else:
                    print(i, end=" ")

        print("")
        casos += 1

    except:
        break
