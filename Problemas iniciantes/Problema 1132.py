x = int(input())
y = int(input())

lista = [x,y]
lista.sort()

soma = list()
total = 0

if lista[1]%13 == 0:
    for i in range(lista[0],lista[1]):
        if i%13 != 0:
            soma.append(i)
        else:
            continue
else:
    for i in range(lista[0], lista[1]+1):
        if i%13 != 0:
            soma.append(i)
        else:
            continue

for i in soma:
    total += i

print(total)
