import math

n = int(input())

positivo = ((1+math.sqrt(5))/2)**n
negativo = ((1-math.sqrt(5))/2)**n

print("{:.1f}". format((positivo - negativo)/math.sqrt(5)))
