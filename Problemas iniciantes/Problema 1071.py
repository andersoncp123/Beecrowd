x = int(input())
y = int(input())
cont = 0

lista = [x,y]
lista.sort(reverse=True)

X = lista[0]
Y = lista[1]

for i in range(Y+1, X):
    if i%2 != 0:
       cont += i
print(cont)
