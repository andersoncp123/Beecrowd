x = int(input())
z = int(input())
soma = 0
count = 0

while z <= x:
    z = int(input())

for i in range(x,z+1):
    soma += i

    if soma < z:
        count += 1
    else:
        continue

print(count+1)
