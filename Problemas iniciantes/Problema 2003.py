try:
    while True:
        ent = list(map(int,input().strip().split(":")))

        if ent[0] < 7:
            print("Atraso maximo: 0")

        else:
            if ent[0] > 7:
                atraso = (ent[0] - 7) * 60
                print("Atraso maximo: {}".format(atraso + ent[1]))
            elif ent[1] == 30:
                print("Atraso maximo: 30")
            elif ent[1] == 0:
                print("Atraso maximo: 0")
            elif ent[1] > 0:
                print("Atraso maximo: {}".format(ent[1]))
except:
    EOFError
