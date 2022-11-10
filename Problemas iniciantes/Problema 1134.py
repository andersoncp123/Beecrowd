x = 0
al = 0
ga = 0
di = 0

while True:
    x = int(input())

    if x < 0 or x > 4:
        continue

    else:
        if x == 1:
            al += 1

        elif x == 2:
            ga += 1

        elif x == 3:
            di += 1

        elif x == 4:
            break

print("MUITO OBRIGADO")
print("Alcool: {}". format(al))
print("Gasolina: {}". format(ga))
print("Diesel: {}". format(di))
