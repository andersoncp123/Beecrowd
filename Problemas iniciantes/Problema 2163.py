ent = list(map(int,input().strip().split()))

matriz = []
corL = 0
corC = 0

for l in range(ent[0]):
    linha = []
    for c in range(1):
        linha = list(map(int,input().strip().split())) [:ent[1]]
    matriz.append(linha)

for l in range(1,ent[0]-1):
    for c in range(1,ent[1]-1):
        if matriz[l][c] == 42:
            if matriz[l-1][c] == 7 and matriz[l+1][c] == 7 and matriz[l-1][c-1] == 7 and matriz[l+1][c+1] == 7 and matriz[l][c+1] == 7 and matriz[l][c-1] == 7 and matriz[l-1][c+1] == 7 and matriz[l+1][c-1] == 7:
                corL = l
                corC = c

if corL == 0 and corC == 0:
    print(corL, corC)
else:
    print(corL+1, corC+1)
