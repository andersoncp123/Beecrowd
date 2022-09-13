selecao = input(). split()

a = int(selecao[0])
b = int(selecao[1])
c = int(selecao[2])
d = int(selecao[3])

if b > c and d > a and (c + d) > (a + b) and ( c and d > 0 ) and a//2:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
