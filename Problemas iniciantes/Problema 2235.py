ent = list(map(int,input().strip().split()))

if ent[0] == ent[1] or ent[0] == ent[2] or ent[1] == ent[2]:
    print("S")

elif ent[0] + ent[1] == ent[2]:
    print("S")

elif ent[0] + ent[2] == ent[1]:
    print("S")

elif ent[1] + ent[2] == ent[0]:
    print("S")

else:
    print("N")
