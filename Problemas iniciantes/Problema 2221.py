b = int(input())

for i in range(b):
    bonus = int(input())
    ent1 = list(map(int,input().strip().split()))
    ent2 = list(map(int,input().strip().split()))

    if ent1[2] % 2 == 0:
        ataqueD = ((ent1[0]+ent1[1])/2) + bonus
    else:
        ataqueD = ((ent1[0] + ent1[1]) / 2)

    if ent2[2] % 2 == 0:
        ataqueG = ((ent2[0] + ent2[1]) / 2) + bonus
    else:
        ataqueG = ((ent2[0] + ent2[1]) / 2)

    if ataqueD > ataqueG:
        print("Dabriel")
    elif ataqueG > ataqueD:
        print("Guarte")
    else:
        print("Empate")
