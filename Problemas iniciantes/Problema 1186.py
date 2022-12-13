ope = input()
media = 0
soma = 0
k = 12
matriz = []

for i in range(12):
    linha= []
    for j in range(12):
        linha.append(eval(input()))
    matriz.append(linha)

if ope == "M":
    for i in range(1,12):
        k -= 1
        for c in range(12,k,-1):
            media = media + matriz[i][c-1]
    media = media/66
    print("{:.1f}". format(media))

elif ope == "S":
    for i in range(1,12):
        k -= 1
        for c in range(12,k,-1):
            soma = soma + matriz[i][c-1]
    print("{:.1f}". format(soma))
