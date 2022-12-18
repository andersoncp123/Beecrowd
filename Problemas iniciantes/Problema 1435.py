n = 1
lista = []

while True:
    t = int(input())
    if t == 0:
        break
    else:
        lista.append(t)
for n in lista:
    m = 1
    direita = n - 1
    esquerda = 0
    cima = 0
    baixo = n - 1
    matriz = [1] * n
    for i in range(n):
        matriz[i] = [1] * n
    if n%2 == 0:
        meio = n / 2
    else:
        meio = (n + 1) / 2
    while m <= meio:
        i = esquerda
        while i <= direita:
            matriz[cima][i] = m
            matriz[baixo][i] = m
            i += 1
        i = cima + 1
        while i < baixo:
            matriz[i][esquerda] = m
            matriz[i][direita] = m
            i += 1
        m += 1
        direita -= 1
        esquerda += 1
        cima += 1
        baixo -= 1
    for i in range(n):
        for j in range(n):
            if matriz[i][j] < 10:
                print("  ", end="")
            elif matriz[i][j] < 100:
                print(" ", end="")
            if j == n - 1:
                print(f"{matriz[i][j]}")
            else:
                print(f"{matriz[i][j]}", end = " ")    
    print()
