ope = input()
media = 0
soma = 0
k = -1
count = 0
matriz = []

for i in range(12):
    linha= []
    for j in range(12):
        linha.append(eval(input()))
    matriz.append(linha)

if ope == "M":
    for i in range(1,11):
        if i < 5:
            k += 1
        elif i == 5 or i == 6:
            k = 4
        else:
            k -= 1
        for c in range(k+1):
            media = media + matriz[i][c]
            count += 1
    media = media/count
    print("{:.1f}". format(media))

elif ope == "S":
    for i in range(1,11):
        if i < 5:
            k += 1
        elif i == 5 or i == 6:
            k = 4
        else:
            k -= 1
        for c in range(k+1):
            soma = soma + matriz[i][c]
    print("{:.1f}". format(soma))
