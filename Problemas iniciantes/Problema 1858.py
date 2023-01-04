n = int(input())

pessoas = list(map(int,input().strip().split())) [:n]

x = pessoas.copy()

pessoas.sort()

print(x.index(pessoas[0])+1)
