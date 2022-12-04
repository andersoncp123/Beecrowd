t = int(input())
x = []

for i in range(1000):
    for k in range(t):
        x.append(k)

for i in range(1000):
    print("N[{}] = {}". format(i, x[i]))
