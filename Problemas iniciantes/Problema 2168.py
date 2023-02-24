n = int(input())

matriz = []

for l in range(n+1):
    ent = []
    for c in range(1):
        ent = list(map(int,input().strip().split())) [:n+1]
    matriz.append(ent)

for x in range(n):
    for y in range(n):
        if(int(matriz[x][y]) + int(matriz[x][y+1]) + int(matriz[x+1][y]) + int(matriz[x+1][y+1]) < 2):
            print("U", end="")
        else:
            print("S", end="")
    print()
