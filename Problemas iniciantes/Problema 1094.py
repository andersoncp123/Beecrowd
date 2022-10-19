c = int(input())
cont = 0
soma = 0
coelhos = 0
ratos = 0
sapos = 0

while(cont != c):
    ent = input().split()
    a = int(ent[0])
    b = str(ent[1])
    cont += 1
    soma += a
    
    if b == "C":
        coelhos += a
        
    elif b == "R":
        ratos += a
        
    elif b == "S":
        sapos += a

print("Total: {} cobaias". format(soma))
print("Total de coelhos: {}". format(coelhos))
print("Total de ratos: {}". format(ratos))
print("Total de sapos: {}". format(sapos))
print("Percentual de coelhos: {:.2f} %". format(coelhos*100/soma))
print("Percentual de ratos: {:.2f} %". format(ratos*100/soma))
print("Percentual de sapos: {:.2f} %". format(sapos*100/soma))
