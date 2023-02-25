while True:
    ent = list(map(int,input().strip().split()))

    if ent[0] == 0 and ent[1] == 0:
        break

    else:
        print(ent[1]*ent[0])
