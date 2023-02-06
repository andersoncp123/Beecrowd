while True:
    ent = input().split()
    n = int(ent[0])
    m = int(ent[1])

    notas = [2, 5, 10, 20, 50, 100]
    pagar = m - n
    verificar = 0

    if n == 0 and m == 0:
        break

    else:
        if pagar > 100:
            pagar -= 100
            for i in range(6):
                if pagar == notas[i]:
                    verificar = 1

        elif pagar > 50:
            pagar -= 50
            for i in range(6):
                if pagar == notas[i]:
                    verificar = 1
        elif pagar > 20:
            pagar -= 20
            for i in range(6):
                if pagar == notas[i]:
                    verificar = 1
        elif pagar > 10:
            pagar -= 10
            for i in range(6):
                if pagar == notas[i]:
                    verificar = 1
        elif pagar > 5:
            pagar -= 5
            for i in range(6):
                if pagar == notas[i]:
                    verificar = 1
        elif pagar > 2:
            pagar -= 2
            for i in range(6):
                if pagar == notas[i]:
                    verificar = 1

        if verificar == 1:
            print("possible")
        else:
            print("impossible")
