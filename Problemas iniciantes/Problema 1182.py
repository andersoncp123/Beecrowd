n = int(input())

ope = input()

media = 0
soma = 0
matriz = []

for i in range(12):
    linha = []
    for j in range(12):
        linha.append(eval(input()))
    matriz.append(linha)

if ope == "M":
    for c in range(12):
        media = media + matriz[c][n]
    media = media/12
    print("{:.1f}". format(media))

elif ope == "S":
    for c in range(12):
        soma = soma + matriz[c][n]
    print("{:.1f}". format(soma))
