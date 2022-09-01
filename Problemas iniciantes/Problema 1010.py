prod1 = input().split()

cod1 = prod1[0]
num1 = int(prod1[1])
valor1 = float(prod1[2])

prod2 = input().split()

cod2 = prod2[0]
num2 = int(prod2[1])
valor2 = float(prod2[2])

Tvalor = (num1*valor1)+(num2*valor2)

print("VALOR A PAGAR: R$ {:.2f}". format(Tvalor))
