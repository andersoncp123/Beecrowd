x = 1
y = 2
g = 3
cont = 0

while(cont < 20):
    x = x + g/y
    g += 2
    y *= 2
    cont += 1
print("{:.2f}". format(x))
