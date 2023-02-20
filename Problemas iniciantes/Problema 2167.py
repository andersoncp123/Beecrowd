n = int(input())
velo = list(map(int,input().strip().split())) [:n]

count = -1
error = 0

for i in velo:
    count += 1
    if i == velo[0]:
        continue
    else:
        if i < velo[count-1]:
            error = count
            break

if error == 0:
    print(error)
else:
    print(error+1)
