while True:
    try:
        xy = list(map(int,input().strip().split()))
        
        matriz = []
        casos = []
        casos2 = []
        
        for l in range(xy[0]):
            linha = []
            for c in range(1):
                ent2 = list(map(int,input().strip().split()))
        
            matriz.append(ent2)
        
        for l in range(xy[0]):
            for c in range(xy[1]):
                if matriz[l][c] == 2:
                    casos.insert(0, l)
                    casos.insert(1, c)
                if matriz[l][c] == 1:
                    casos2.insert(0, l)
                    casos2.insert(1, c)
                    
        print(abs(int(casos[0]) - int(casos2[0])) + abs(int(casos[1]) - int(casos2[1])))
    except:
        break
