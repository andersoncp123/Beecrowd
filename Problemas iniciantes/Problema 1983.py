n = int(input())
notas = list()
notascopy = list()
alunos = list()

for i in range(n):
    ent = input().split()
    a = int(ent[0])
    b = float(ent[1])

    alunos.append(a)
    notas.append(b)
    notascopy.append(b)
    notas.sort()
    
if notas[-1] >= 8:
    index = notascopy.index(notas[-1])
    print(alunos[index])
else:
    print("Minimum note not reached")
