while True:
    try:
        ent = input().split()
        mes = int(ent[0])
        dia = int(ent[1])

        dias = 360
        tempo = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]

        if mes == 12 and dia == 25:
            print("E natal!")

        elif mes == 12 and dia == 24:
            print("E vespera de natal!")

        elif mes == 12 and dia > 25:
            print("Ja passou!")

        else:
            for i in range(mes):
                if i == 0:
                    dias -= dia
                else:
                    dias -= tempo[i]
            print("Faltam {} dias para o natal!". format(dias))

    except EOFError:
        break
