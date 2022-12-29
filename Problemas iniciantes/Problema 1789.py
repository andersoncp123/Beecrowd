while True:
    try:
        l = int(input())

        velocidade = list(map(int, input().strip().split())) [:l]
        velocidade.sort()

        if velocidade[-1] < 10:
            print(1)
        elif 10 <= velocidade[-1] < 20:
            print(2)
        elif velocidade[-1] >= 20:
            print(3)

    except EOFError:
        break
