val = input().split()

a = int(val[0])
b = int(val[1])

if a < b:
    print("O JOGO DUROU {} HORA(S)". format(b-a))

else:
    print("O JOGO DUROU {} HORA(S)". format((24-a)+b))
