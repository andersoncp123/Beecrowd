while True:
    try:
        n = int(input())
        matriz = [3] * n
        for i in range(n):
            matriz[i] = [3] * n
        for i in range(n):
            for j in range(n):
                if i == j:
                    matriz[i][j] = 1
        a = n
        for i in range(n):
            for j in range(n):
                if j == n - 1:
                    matriz[i][j] = 2
            n -= 1
        for i in range(a):
            for j in range(a):
                print(f"{matriz[i][j]}", end="")
            print()
    except:
        break
