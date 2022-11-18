n = int(input())
x = 0
y = 1
for i in range(n):
    if i == n-1:
        print(x)
    else:
        print(x, end=" ")
        t = x + y
        x = y
        y = t
