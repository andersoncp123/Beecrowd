import math

n = int(input())

p = n/math.log(n)

m = 1.25506 * (n/math.log(n))

print("{:.1f} {:.1f}".format(p,m))
