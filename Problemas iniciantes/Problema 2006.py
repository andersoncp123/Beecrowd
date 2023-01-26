cha = int(input())
respostas = list(map(int,input().strip().split()))

count = 0

for i in respostas:
    if i == cha:
        count += 1

print(count)
