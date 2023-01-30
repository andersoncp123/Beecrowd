horario = list(map(int,input().strip().split()))

hora = horario[0] + horario[1] + horario[2]

if hora < 0:
    print(24 + hora)

elif hora == 24:
    print(0)

elif hora > 24:
    print(hora - 24)

else:
    print(hora)
