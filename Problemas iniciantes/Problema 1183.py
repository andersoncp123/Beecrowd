ope = input()
media = 0
soma = 0
k = 0
matriz = []

for i in range(12):
    linha= []
    for j in range(12):
        linha.append(eval(input()))
    matriz.append(linha)

if ope == "M":
    for i in range(12):
        k += 1
        for c in range(k,12):
            media = media + matriz[i][c]
    media = media/66
    print("{:.1f}". format(media))

elif ope == "S":
    for i in range(12):
        k += 1
        for c in range(k,12):
            soma = soma + matriz[i][c]
    print("{:.1f}". format(soma))
