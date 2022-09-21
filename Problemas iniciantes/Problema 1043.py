import math
tri = input(). split()

a = float(tri[0])
b = float(tri[1])
c = float(tri[2])

if  abs(b - c) < a < b + c:
    peri = a+b+c
    print("Perimetro = {:.1f}". format(peri))
else:
    area = ((a+b)*c)/2
    print("Area = {:.1f}". format(area))
