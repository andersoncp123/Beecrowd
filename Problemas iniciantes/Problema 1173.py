x = []
j = int(input())
x.append(j)

for i in range(10):
    y = x[i] * 2
    x.append(y)

for i in range(10):
    print("N[{}] = {}". format(i, x[i]))
