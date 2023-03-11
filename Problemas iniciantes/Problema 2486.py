while True:
    soma = 0
    ent = int(input())

    if ent == 0:
        break

    else:
        for i in range(ent):

            alimentos = input().split()

            quantidade, comida = int(alimentos[0]),alimentos[1]

            if comida == "suco":
                soma += 120*quantidade
            if comida == "morango":
                soma += 85 * quantidade
            if comida == "mamao":
                soma += 85 * quantidade
            if comida == "goiaba":
                soma += 70 * quantidade
            if comida == "manga":
                soma += 56 * quantidade
            if comida == "laranja":
                soma += 50 * quantidade
            if comida == "brocolis":
                soma += 34 * quantidade
        if soma < 110:
            print("Mais {} mg".format(110-soma))
        elif soma > 130:
            print("Menos {} mg".format(soma - 130))
        else:
            print("{} mg".format(soma))
