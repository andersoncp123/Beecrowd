ent = int(input())

for i in range(ent):
    p1 = input()
    p2 = input()

    if p1 == "ataque" and p2 == "ataque":
        print("Aniquilacao mutua")

    elif p1 == "pedra" and p2 == "pedra":
        print("Sem ganhador")

    elif p1 == "papel" and p2 == "papel":
        print("Ambos venceram")

    elif p1 == "ataque" and (p2 == "papel" or p2 == "pedra"):
        print("Jogador 1 venceu")

    elif p1 == "pedra" and p2 == "papel":
        print("Jogador 1 venceu")

    else:
        print("Jogador 2 venceu")
