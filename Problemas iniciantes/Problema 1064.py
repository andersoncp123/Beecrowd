positivos = 0
soma = 0

for i in range(6):
    x = float(input())
    if x > 0:
        positivos += 1
        soma += x

    
        
print("{} valores positivos". format(positivos))
print("{:.1f}". format(soma/positivos))
