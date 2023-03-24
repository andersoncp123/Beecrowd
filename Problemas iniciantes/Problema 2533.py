while True:
    try:
        m = int(input())
        somaNumerado = 0
        somaDenominador = 0
        for i in range(m):
            num = list(map(int,input().strip().split()))
            somaNC = num[0]*num[1]

            somaNumerado += somaNC
            somaDenominador += num[1]

        print("{:.4f}".format(somaNumerado / (somaDenominador * 100)))
    except:
        break
