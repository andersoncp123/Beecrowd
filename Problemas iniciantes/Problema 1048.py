val = float(input())

por15 = val*0.15
por12 = val*0.12
por10 = val*0.10
por7 = val*0.07
por4 = val*0.04

if 0 <= val <= 400.00:
    print("Novo salario: {:.2f}". format(val+por15))
    print("Reajuste ganho: {:.2f}". format(por15))
    print("Em percentual: 15 %")
elif 400.01 <= val <= 800.00:
    print("Novo salario: {:.2f}". format(val+por12))
    print("Reajuste ganho: {:.2f}". format(por12))
    print("Em percentual: 12 %")
elif 800.01 <= val <= 1200.00:
    print("Novo salario: {:.2f}". format(val+por10))
    print("Reajuste ganho: {:.2f}". format(por10))
    print("Em percentual: 10 %")
elif 1200.01 <= val <= 2000.00:
    print("Novo salario: {:.2f}". format(val+por7))
    print("Reajuste ganho: {:.2f}". format(por7))
    print("Em percentual: 7 %")
else:
    print("Novo salario: {:.2f}". format(val+por4))
    print("Reajuste ganho: {:.2f}". format(por4))
    print("Em percentual: 4 %")
