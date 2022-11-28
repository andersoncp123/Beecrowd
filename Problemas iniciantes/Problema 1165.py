n = int(input())
count = 0

while count < n:
    x = int(input())
    count += 1
    list = []

    for i in range(1,x+1):
        if x%i == 0:
            list.append(i)

    if len(list) > 2:
        print(x,"nao eh primo")
    else:
        print(x,"eh primo")
