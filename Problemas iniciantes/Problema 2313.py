ent = list(map(int,input().strip().split()))

a, b, c = ent[0], ent[1], ent[2]

true = 0
lado1 = abs(b - c) < a < b + c
lado2 = abs(a - c) < b < a + c
lado3 = abs(a - b) < c < a + b

if lado1 != True and lado2 != True and lado3 != True:
    print("Invalido")
else:
    if a == b == c:
        print("Valido-Equilatero")
    elif a != b and b != c and a != c:
        print("Valido-Escaleno")
    else:
        print("Valido-Isoceles")

    numeros = [a,b,c]
    numeros.sort()

    if numeros[-1]**2 == numeros[0]**2 + numeros[1]**2:
        print("Retangulo: S")
    else:
        print("Retangulo: N")
