n = int(input())
total = 0

for i in range(n):
    ent = list(map(int,input().strip().split()))

    if ent[0] == 1001:
        total += (1.50 * ent[1])

    elif ent[0] == 1002:
        total += (2.50 * ent[1])

    elif ent[0] == 1003:
        total += (3.50 * ent[1])

    elif ent[0] == 1004:
        total += (4.50 * ent[1])

    else:
        total += (5.50 * ent[1])

print("{:.2f}". format(total))
