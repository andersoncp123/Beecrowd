x = []

for i in range(10):
    x.append(int(input()))

for i in range(10):
    if x[i] <= 0:
        print("X[{}] = 1". format(i))
    else:
        print("X[{}] = {}". format(i, x[i]))
