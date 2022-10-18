numeros = list()

for i in range(100):
    x = int(input())

    numeros.append(x)

numeros2 = numeros.copy()

numeros.sort(reverse=True)

print(numeros[0])
print(numeros2.index(numeros[0])+1)
