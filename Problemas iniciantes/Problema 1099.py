z = int(input())

for i in range(z):
    ent = input().split()
    x = int(ent[0])
    y = int(ent[1])

    lista = [x,y]
    lista.sort(reverse=True)

    X = lista[0]
    Y = lista[1]
    cont = 0
    for i in range(Y+1, X):
        if i%2 != 0:
           cont += i
    print(cont)
