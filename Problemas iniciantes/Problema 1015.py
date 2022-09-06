import math

pont1 = input(). split()

x1 = float(pont1[0])
y1 = float(pont1[1])

pont2 = input(). split()

x2 = float(pont2[0])
y2 = float(pont2[1])

Dis = math.sqrt((x2-x1)**2+(y2-y1)**2)

print("{:.4f}". format(Dis))
