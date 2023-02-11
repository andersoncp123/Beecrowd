t = int(input())

for i in range(t):
    ent = list(map(int,input().strip().split()))

    if ent[0] < 10:
        ent[0] = "0" + str(ent[0])

    if ent[1] < 10:
        ent[1] = "0" + str(ent[1])

    if ent[2] == 1:
        print("{}:{} - A porta abriu!". format(ent[0],ent[1]))
    else:
        print("{}:{} - A porta fechou!".format(ent[0], ent[1]))
