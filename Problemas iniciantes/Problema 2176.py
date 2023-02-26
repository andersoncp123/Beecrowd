ent = input()

count = 0

for i in range(len(ent)):
    if ent[i] == "1":
        count += 1

if count % 2 == 0:
    print(ent + "0")
else:
    print(ent + "1")
