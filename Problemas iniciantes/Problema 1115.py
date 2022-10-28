while True:
    ent = input().split()

    x = int(ent[0])
    y = int(ent[1])

    if x == 0 or y ==  0:
        break

    else:
        if x > 0 and y > 0:
            print("primeiro")

        elif x > 0 and y < 0:
            print("quarto")

        elif x < 0 and y > 0:
            print("segundo")

        elif x < 0 and y < 0:
            print("terceiro")
