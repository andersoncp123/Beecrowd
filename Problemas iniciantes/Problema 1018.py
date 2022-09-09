notas = int(input())

print(notas)

n100 = notas//100
notas = notas%100

n50 = notas//50
notas = notas%50

n20 = notas//20
notas = notas%20

n10 = notas//10
notas = notas%10

n5 = notas//5
notas = notas%5

n2 = notas//2
notas = notas%2

print("{} nota(s) de R$ 100,00". format(n100))
print("{} nota(s) de R$ 50,00". format(n50))
print("{} nota(s) de R$ 20,00". format(n20))
print("{} nota(s) de R$ 10,00". format(n10))
print("{} nota(s) de R$ 5,00". format(n5))
print("{} nota(s) de R$ 2,00". format(n2))
print("{} nota(s) de R$ 1,00". format(notas))
