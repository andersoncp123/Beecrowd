import re
while True:
    try:
        t = int(input())

        operacoes = []
        naoPassou = []

        for i in range(t):
            a = input()
            a = a.split()
            b = re.split("=",a[1])
            b.insert(0,a[0])
            b[0] = int(b[0])
            b[1] = int(b[1])
            b[2] = int(b[2])
            operacoes.append(b)

        for i in range(t):
            ent = input().split()

            nome, indice, sinal = ent[0], int(ent[1]), ent[2]

            if sinal == "+":
                if operacoes[indice - 1][0] + operacoes[indice - 1][1] == operacoes[indice - 1][2]:
                    continue
                else:
                    naoPassou.append(nome)
            elif sinal == "*":
                if operacoes[indice - 1][0] * operacoes[indice - 1][1] == operacoes[indice - 1][2]:
                    continue
                else:
                    naoPassou.append(nome)
            elif sinal == "-":
                if operacoes[indice - 1][0] - operacoes[indice - 1][1] == operacoes[indice - 1][2]:
                    continue
                else:
                    naoPassou.append(nome)
            elif sinal == "I":
                if operacoes[indice - 1][0] + operacoes[indice - 1][1] == operacoes[indice - 1][2]:
                    naoPassou.append(nome)
                if operacoes[indice - 1][0] - operacoes[indice - 1][1] == operacoes[indice - 1][2]:
                    naoPassou.append(nome)
                if operacoes[indice - 1][0] * operacoes[indice - 1][1] == operacoes[indice - 1][2]:
                    naoPassou.append(nome)

        if len(naoPassou) == t:
            print("None Shall Pass!")

        elif len(naoPassou) == 0:
            print("You Shall All Pass!")

        else:
            naoPassou.sort()
            for i in range(len(naoPassou)):
                if i == len(naoPassou)-1:
                    print(naoPassou[i])
                else:
                    print(naoPassou[i],end=" ")
    except:
        break
