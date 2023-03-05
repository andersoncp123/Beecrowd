jogadores = int(input())

listaNotas = []
listaNomes = []

for i in range(jogadores):
    soma = 0
    nome = input()
    peso = float(input())
    notas = list(map(float,input().strip().split()))

    notas.sort()
    notas.pop(0)
    notas.pop(-1)

    for i in notas:
        soma += i
    listaNotas.append(soma*peso)
    listaNomes.append(nome)


for i in range(len(listaNotas)):
    print("{} {:.2f}".format(listaNomes[i],listaNotas[i]))
