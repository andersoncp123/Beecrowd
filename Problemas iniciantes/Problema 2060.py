n = int(input())
ent = list(map(int,input().strip().split())) [:n]

multi2 = 0
multi3 = 0
multi4 = 0
multi5 = 0

for i in ent:
    if i % 2 == 0:
        multi2 += 1

    if i % 3 == 0:
        multi3 += 1

    if i % 4 == 0:
        multi4 += 1

    if i % 5 == 0:
        multi5 += 1

print("{} Multiplo(s) de 2". format(multi2))
print("{} Multiplo(s) de 3". format(multi3))
print("{} Multiplo(s) de 4". format(multi4))
print("{} Multiplo(s) de 5". format(multi5))
