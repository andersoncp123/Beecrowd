while True:
    t = int(input())

    if t == 0:
        break

    for i in range(t):
        n = int(input())

        soma = 0

        if n  % 2 == 0:
            soma = soma + ((n - 2) * 2) + 2
            print(soma)
        else:
            soma = soma + ((n - 1) * 2) + 1
            print(soma)
