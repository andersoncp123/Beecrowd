sal = float(input())

if sal <= 2000.00:
    print("Isento")

elif sal >= 2000.01 and sal <= 3000.00:
    x = (sal - 2000)*0.08
    print("R$ {:.2f}".format(x))

elif sal >= 3000.01 and sal <=4500.00:
    x = (sal - 3000)*0.18 + 1000*0.08
    print("R$ {:.2f}".format(x))

elif sal > 4500.00:
    x = (sal-4500)*0.28 + 1500*0.18 + 1000*0.08
    print("R$ {:.2f}".format(x))
