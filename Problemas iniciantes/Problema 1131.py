inter = 0
gremio = 0
empate = 0
grenais = 0
x = 0

while(x != 2):
    ent = input().split()
    a = int(ent[0])
    b = int(ent[1])

    if a > b:
        inter += 1

    elif b > a:
        gremio += 1

    elif a == b:
        empate += 1

    print("Novo grenal (1-sim 2-nao)")
    j = int(input())

    if j == 1:
        x = 1

    elif j == 2:
        x = 2

grenais += inter + gremio + empate

print("{} grenais". format(grenais))
print("Inter:{}". format(inter))
print("Gremio:{}". format(gremio))
print("Empates:{}". format(empate))

if inter > gremio:
    print("Inter venceu mais". format(grenais))
elif gremio > inter:
    print("Gremio venceu mais". format(grenais))
elif inter == gremio:
    print("Nao houve vencedor")
