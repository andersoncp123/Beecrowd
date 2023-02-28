import math
while True:
    try:
        ent = list(map(int,input().strip().split()))
        #Xf ent[0] Yf ent[1] Xi ent[2] Yi ent[3] Vi ent[4] R1 ent[5] R2 ent[6]

        raio = ent[5] + ent[6]
        distancia = math.sqrt(pow((ent[0] - ent[2]), 2) + pow((ent[1] - ent[3]), 2))

        if distancia + 1.5*ent[4] <= raio:
            print("Y")
        else:
            print("N")

    except EOFError:
        break
