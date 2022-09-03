ar = input(). split()

a = float(ar[0])
b = float(ar[1])
c = float(ar[2])

pi = 3.14159

AT = (a*c)/2
AC = pi*c**2
APezio = ((a+b)*c)/2
AQua = b**2
ARe = a*b

print("TRIANGULO: {:.3f}". format(AT))
print("CIRCULO: {:.3f}". format(AC))
print("TRAPEZIO: {:.3f}". format(APezio))
print("QUADRADO: {:.3f}". format(AQua))
print("RETANGULO: {:.3f}". format(ARe))
