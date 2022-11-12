n = int(input())

u = 0
i = 0
o = 0
cont = 1

while(cont <= n):
    u = u+1
    i = u**2
    o = u**3
    print("{} {} {}". format(u,i,o))
    cont = cont+1
