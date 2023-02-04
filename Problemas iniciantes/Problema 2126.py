casos = 0
while True:
    try:
        casos += 1

        n1 = input()
        n2 = input()

        countSub = n2.count(n1)

        if countSub == 0:
            print("Caso #{}:". format(casos))
            print("Nao existe subsequencia")

        else:
            print("Caso #{}:".format(casos))
            print("Qtd.Subsequencias: {}".format(countSub))
            countSub = n2.rfind(n1)
            print("Pos: {}".format((int(countSub) + 1)))
        print()

    except EOFError:
        break
