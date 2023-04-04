while True:
    try:
        ent = list(map(int,input().strip().split()))

        soma = 0

        for i in range(ent[0]):
            identificador = list(map(int,input().strip().split()))

            if identificador[0] == ent[1]:
                if identificador[1] == 0:
                    soma += 1

        print(soma)
    except:
        break
