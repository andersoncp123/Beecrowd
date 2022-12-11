ope = input()
media = 0
soma = 0
k = 1
p = 0
matriz = []

for i in range(12):
    linha= []
    for j in range(12):
        linha.append(eval(input()))
    matriz.append(linha)

if ope == "M":
    for i in range(k, 12):
        k += 1
        p += 1
        for c in range(0, p):
            media = media + matriz[i][c]
    media = media/66
    print("{:.1f}". format(media))

elif ope == "S":
    for i in range(k,12):
        k += 1
        p += 1
        for c in range(0,p):
            soma = soma + matriz[i][c]
    print("{:.1f}". format(soma))
