while True:
    try:
        ent = list(map(int,input().strip().split()))

        soma = 0

        for i in range(ent[0]):
            altura = int(input())

            if ent[1] <= altura <= ent[2]:
                soma += 1

        print(soma)
    except:
        break
