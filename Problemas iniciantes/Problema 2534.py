while True:
    try:
        notas = []

        ent = list(map(int,input().strip().split()))

        for i in range(ent[0]):
            nota = int(input())
            notas.append(nota)

        notas.sort(reverse=True)

        for j in range(ent[1]):
            posi = int(input())

            print(notas[posi-1])
    except:
        break
