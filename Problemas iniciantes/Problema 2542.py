while True:
    try:
        n = int(input())
        ent = list(map(int,input().strip().split()))

        j1 = []
        j2 = []

        for i in range(ent[0]):
            j1.append([int(x) for x in input().split()])
        for i in range(ent[1]):
            j2.append([int(x) for x in input().split()])

        cm, cl = [int(x) for x in input().split()]
        a = int(input())

        if j1[cm-1][a-1] > j2[cl-1][a-1]:
            print("Marcos")
        elif j1[cm-1][a-1] == j2[cl-1][a-1]:
            print("Empate")
        else:
            print("Leonardo")
    except:
        break
