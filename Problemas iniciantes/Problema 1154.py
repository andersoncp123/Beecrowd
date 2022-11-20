soma = 0
idades = list()

while True:
    x = int(input())

    if x > 0:
        idades.append(x)
    else:
        break

for i in idades:
    soma += i

print("{:.2f}". format(soma/len(idades)))
