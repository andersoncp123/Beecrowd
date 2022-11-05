count = 0
notas = list()

while count != 2:
    nota = float(input())

    if nota < 0 or nota > 10:
        print("nota invalida")

    else:
        count += 1
        notas.append(nota)

print("media = {:.2f}". format((notas[0]+notas[1])/2))
