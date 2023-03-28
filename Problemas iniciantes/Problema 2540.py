while True:
    try:
        ent = int(input())
        votos = list(map(float,input().strip().split()))

        sim = 0

        for i in votos:
            if i == 1:
                sim += 1

        if sim >= ent * (2/3):
            print("impeachment")
        else:
            print("acusacao arquivada")
    except:
        break
