x = int(input())
count = 0

while count < x:
    anos = 0

    ent = input().split()

    pa = int(ent[0])
    pb = int(ent[1])
    g1 = float(ent[2])
    g2 = float(ent[3])

    while int(pa) <= int(pb):
        pa += int((g1/100)*pa)
        pb += int((g2/100)*pb)
        anos += 1
        if anos > 100:
            break

    count += 1

    if anos > 100:
        print("Mais de 1 seculo.")
    else:
        print(anos,"anos.")
