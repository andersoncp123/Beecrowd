numero = int(input())
numero = str(numero)

k = 1

for i in range(len(numero)):
    if i == len(numero)-1:
        print(numero[i-k])
    else:
        print(numero[i-k], end="")
    k += 2
