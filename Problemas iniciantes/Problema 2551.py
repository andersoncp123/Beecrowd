while True:
    try:
        casos = int(input())

        tempo, km, treino = 0, 0, 0

        for i in range(casos):
            ent = list(map(int,input().strip().split()))

            treino += 1

            if tempo == 0 and km == 0:
                print(treino)
                tempo = ent[0]
                km = ent[1]
                media = km/tempo

            else:
                if ent[1]/ent[0] > media:
                    print(treino)
                    media = ent[1]/ent[0]
    except:
        break
