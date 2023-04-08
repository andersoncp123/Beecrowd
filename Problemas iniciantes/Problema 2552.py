while True:
    try:
        matriz = []
        p = 0

        ent1 = list(map(int,input().strip().split()))

        for i in range(ent1[0]):
            for i in range(1):
                ent2 = list(map(int,input().strip().split())) [:ent1[1]]
            matriz.append(ent2)

        for l in range(ent1[0]):
            for c in range(ent1[1]):
                if matriz[l][c] == 1:
                    matriz[l][c] = 9

        for l in range(ent1[0]):
            for c in range(ent1[1]):
                if matriz[l][c] != 9:
                    if l > 0 and matriz[l-1][c] == 9:
                        p += 1
                    if l < ent1[0]-1 and matriz[l+1][c] == 9:
                        p += 1
                    if c > 0 and matriz[l][c-1] == 9:
                        p += 1
                    if c < ent1[1]-1 and matriz[l][c+1] == 9:
                        p += 1
                    matriz[l][c] = p
                    p = 0

                if c != ent1[1]-1:
                    print(matriz[l][c], end="")
                else:
                    print(matriz[l][c])
    except:
        break
