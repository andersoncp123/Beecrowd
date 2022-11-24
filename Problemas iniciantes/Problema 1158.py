a = int(input())
count = 0

while count < a:
    ent = input().split()
    x = int(ent[0])
    y = int(ent[1])
    soma = 0

    #sendo impar
    if x%2 != 0:
        for i in range(x,x+y*2):
            if i%2 != 0:
                soma += i
    #sendo par
    else:
        for i in range(x+1,x+y*2):
            if i%2 != 0:
                soma += i
    print(soma)
    count += 1
