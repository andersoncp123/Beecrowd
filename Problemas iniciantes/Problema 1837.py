ent = input().split()

a = int(ent[0])
b = int(ent[1])

div = divmod(a, abs(b))

if b < 0:
    print(- div[0], div[1])

else:
    print(div[0], div[1])
