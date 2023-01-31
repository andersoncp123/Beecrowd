ent = input().split()

p = int(ent[0])
j1 = int(ent[1])
j2 = int(ent[2])
r = int(ent[3])
a = int(ent[4])

soma = j1 + j2

def verificar():
    if r == 0 and a == 0:
        if soma % 2 == 0 and p == 1:
            print("Jogador 1 ganha!")
        elif soma % 2 != 0 and p == 0:
            print("Jogador 1 ganha!")
        else:
            print("Jogador 2 ganha!")
    else:
        if r == 1 and a == 1:
            print("Jogador 2 ganha!")
        elif r == 1 and a == 0:
            print("Jogador 1 ganha!")
        elif r == 0 and a == 1:
            print("Jogador 1 ganha!")

verificar()
