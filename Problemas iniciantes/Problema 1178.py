x = []
j = float(input())
x.append(j)

for i in range(100):
    y = x[i]/2
    x.append(y)

for i in range(100):
    print("N[{}] = {:.4f}". format(i, x[i]))
