while True:
    try:
        ent = int(input())
        soma = 0

        while(ent > 1):
            ent //= 2
            soma += 1

        print(soma)

    except:
        break
