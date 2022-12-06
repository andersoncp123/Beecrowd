par = []
impar = []
resultantesP = []
resultantesI = []

for i in range(15):
    j = int(input())

    if j%2 == 0:
        if len(par) >= 5:
            resultantesP.append(j)
        else:
            par.append(j)

    else:
        if len(impar) == 5:
            resultantesI.append(j)
        else:
            impar.append(j)

for i in range(len(impar)):
    print("impar[{}] = {}". format(i, impar[i]))

for i in range(len(par)):
    print("par[{}] = {}". format(i, par[i]))

for i in range(len(resultantesI)):
    print("impar[{}] = {}". format(i,resultantesI[i]))

for i in range(len(resultantesP)):
    print("par[{}] = {}". format(i,resultantesP[i]))
