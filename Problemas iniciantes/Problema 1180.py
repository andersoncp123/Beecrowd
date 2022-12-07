n = int(input())

num = list(map(int, input().strip().split()))[:n]

b = num[0]

num2 = num.copy()
num.sort()
posicao = num2.index(num[0])

print("Menor valor:",num[0])
print("Posicao:", posicao)
