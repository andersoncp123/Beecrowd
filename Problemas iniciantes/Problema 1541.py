while True:
    medidas = list(map(int, input().strip().split()))

    if medidas[0] == 0:
        break

    else:
        area = medidas[0] * medidas[1]

        areaP = (area * 100) / medidas[2]

        areaP = areaP ** (1/2)

        print(int(areaP))
