import math
bas = input(). split()

a = float(bas[0])
b = float(bas[1])
c = float(bas[2])

delta = (b**2)-4*a*c

if delta < 0 or a == 0:
    print("Impossivel calcular")
else:
    x1 = (-b+math.sqrt(delta))/(2*a)
    x2 = (-b-math.sqrt(delta))/(2*a)
    print("R1 = {:.5f}". format(x1))
    print("R2 = {:.5f}". format(x2))
