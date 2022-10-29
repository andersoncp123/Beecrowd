n = int(input())

for i in range(n):
    ent = input().split()

    a = int(ent[0])
    b = int(ent[1])

    if b == 0:
        print("divisao impossivel")
    else:
        print("{:.1f}". format(a/b))
