jogadores = int(input())

saques, defesas, ataques = 0,0,0
saques1, defesas1, ataques1 = 0,0,0

for i in range(jogadores):
    nome = input()
    ent1 = list(map(int, input().strip().split()))
    ent2 = list(map(int, input().strip().split()))

    saques += ent1[0]
    defesas += ent1[1]
    ataques += ent1[2]
    saques1 += ent2[0]
    defesas1 += ent2[1]
    ataques1 += ent2[2]

print("Pontos de Saque: {:.2f} %.". format(saques1/saques*100))
print("Pontos de Bloqueio: {:.2f} %.". format(defesas1/defesas*100))
print("Pontos de Ataque: {:.2f} %.". format(ataques1/ataques*100))
