lanche = input(). split()

cod = int(lanche[0])
quant = int(lanche[1])

if cod == 1:
    valor = 4.00
elif cod == 2:
    valor = 4.50
elif cod == 3:
    valor = 5.00
elif cod == 4:
    valor = 2.00
elif cod == 5:
    valor = 1.50

Tgasto = valor*quant

print("Total: R$ {:.2f}". format(Tgasto))
