n = int(input())

resul = 0

for i in range(n):
    resul = 1/(resul + 6)

print("{:.10f}".format(3+resul))
