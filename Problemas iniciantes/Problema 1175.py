arr = []

for i in range(20):
    arr.append(int(input()))

for j in range(1,21):
    print("N[{}] = {}". format(j-1, arr[-j]))
