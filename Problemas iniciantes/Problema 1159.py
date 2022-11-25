while True:
    x = int(input())
    soma = 0

    if x == 0:
        break

    elif x % 2 == 0:
        for i in range(x, x + 9):
            if i % 2 == 0:
                soma += i
        print(soma)

    elif x % 2 != 0:
        for i in range(x + 1, x + 10):
            if i % 2 == 0:
                soma += i
        print(soma)
