n = int(input())

for i in range(n):
    ano = int(input())

    if ano == 2015:
        print("1 A.C.")

    elif ano > 2015:
        print("{} A.C.".format(ano-2015+1))

    else:
        print("{} D.C.". format(2015-ano))
