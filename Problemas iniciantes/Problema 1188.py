ope = input()
media = 0
soma = 0
k = 0
count = 0
matriz = []

for i in range(12):
    linha= []
    for j in range(12):
        linha.append(eval(input()))
    matriz.append(linha)

if ope == "M":
    for i in range(7,12):
        k += 1
        for c in range(6+k,7+k):
            media = media + matriz[i][c]
            count += 1
    media = media/count
    print("{:.1f}". format(media))

elif ope == "S":
    for i in range(7,12):
        k += 1
        for c in range(6-k,6+k):
            soma = soma + matriz[i][c]
    print("{:.1f}". format(soma))
