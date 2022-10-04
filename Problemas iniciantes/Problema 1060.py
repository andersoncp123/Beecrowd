positivos = 0

for i in range(6):
    x = float(input())
    if x > 0:
        positivos += 1

print("{} valores positivos". format(positivos))
