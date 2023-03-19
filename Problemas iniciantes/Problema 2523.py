while True:
    try:
        numerosLista = []
        letras = []
        lista = input()

        for palavra in lista:
            letras.append(list(palavra))

        vezes = int(input())

        for i in range(1):
            numeros = list(map(int,input().strip().split()))

            for i in range(len(numeros)):
                numerosLista.append(letras[(numeros[i]) - 1][0])

        for i in range(len(numerosLista)):
            if i+1 == len(numerosLista):
                print(numerosLista[i])
            else:
                print(numerosLista[i], end="")

    except:
        break
