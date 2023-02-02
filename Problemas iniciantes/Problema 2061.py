ent = list(map(int,input().strip().split()))

soma = ent[0]

for i in range(ent[1]):
    acao = input()

    if acao == "fechou":
        soma += 1
    else:
        soma -= 1

print(soma)
