ent = list(map(int, input().split()))
count = 1
soma = 0

while ent[count] <= 0:
    if ent[count] <= 0:
        count += 1
    else:
        break

for i in range(ent[count]):
    soma += ent[0] + i

print(soma)
