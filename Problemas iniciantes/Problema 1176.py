n = int(input())
j = []
v = []

for i in range(n):
    x = 0
    y = 1
    k = int(input())
    v.append(k)
    
    for i in range(k):
        t = x + y
        x = y
        y = t
    j.append(x)

for i in range(n):
    print("Fib({}) = {}". format(v[i], j[i]))
