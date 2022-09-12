# -*- coding: utf-8 -*-

notas = float(input())
notas = int(notas * 100)

n100 = notas//10000
notas = notas%10000
n50 = notas//5000
notas = notas%5000
n20 = notas//2000
notas = notas%2000
n10 = notas//1000
notas = notas%1000
n5 = notas//500
notas = notas%500
n2 = notas//200
notas = notas%200

print("NOTAS:")
print("{} nota(s) de R$ 100.00". format(n100))
print("{} nota(s) de R$ 50.00". format(n50))
print("{} nota(s) de R$ 20.00". format(n20))
print("{} nota(s) de R$ 10.00". format(n10))
print("{} nota(s) de R$ 5.00". format(n5))
print("{} nota(s) de R$ 2.00". format(n2))

m1 = notas//100
notas = notas%100
m05 = notas//50
notas = notas%50
m025 = notas//25
notas = notas%25
m010 = notas//10
notas = notas%10
m005 = notas//5
notas = notas%5
m001 = notas//1
notas = notas%1

print("MOEDAS:")

print("{} moeda(s) de R$ 1.00". format(m1))
print("{} moeda(s) de R$ 0.50". format(m05))
print("{} moeda(s) de R$ 0.25". format(m025))
print("{} moeda(s) de R$ 0.10". format(m010))
print("{} moeda(s) de R$ 0.05". format(m005))
print("{} moeda(s) de R$ 0.01". format(m001))
