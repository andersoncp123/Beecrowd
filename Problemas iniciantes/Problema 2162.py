n = int(input())
ent = list(map(int, input().strip().split()))

if n == 2 and ent[0] == ent[1]:
    tru = 0
else:
    tru = 1
    for i in range(1, n-1):
        if not ((ent[i] < ent[i-1] and ent[i] < ent[i+1]) or (ent[i] > ent[i-1] and ent[i] > ent[i+1])):
            tru = 0
            break      
print(tru)
