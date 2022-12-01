x = []

for i in range(100):
    y = float(input())
    x.append(y)

for i in range(100):
    if x[i] <= 10:
        print("A[{}] = {}". format(i , x[i]))
