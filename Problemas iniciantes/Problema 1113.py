while True:
    ent = input().split()

    a = int(ent[0])
    b = int(ent[1])

    if a == b:
        break

    else:
        if a > b:
            print("Decrescente")
        else:
            print("Crescente")
