ent1 = list(map(int,input().strip().split()))
ent2 = list(map(int,input().strip().split())) [:ent1[1]]
count = 0

for i in range(len(ent2)-1):
    if abs(ent2[i] - ent2[i+1]) > ent1[0]:
        count = 1

if count == 1:
    print("GAME OVER")
else:
    print("YOU WIN")
