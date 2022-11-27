n = int(input())
count = 0

while count < n:
    x = int(input())
    soma = 0
    count += 1

    for i in range(1,x):
        if x%i == 0:
            soma += i

    if soma == x:
        print(x,"eh perfeito")
    else:
        print(x,"nao eh perfeito")
