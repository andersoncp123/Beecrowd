x = int(input())
y = int(input())

lista = [x,y]
lista.sort()

num = list()

if x > 0 and y > 0:
    for i in range(lista[0]+1, lista[1]):
        if i % 5 == 2 or i % 5 == 3:
            num.append(i)

    for i in range(len(num)):
        print(num[i])
