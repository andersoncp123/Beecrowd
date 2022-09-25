ent = input().split()

Hi = int(ent[0])
Mi = int(ent[1])
Hf = int(ent[2])
Mf = int(ent[3])

if Hf > Hi:
    T = Hf - Hi

elif Hi > Hf:
    T = (24 - Hi) + Hf

elif Hi == Hf:
    T = 24

if Mf > Mi:
    Tm = Mf - Mi
    if Hi == 0 and Hf == 0:
        T += 1
        if T > 24:
            T = 0

elif Mi > Mf:
    Tm = 60 - (Mi - Mf)
    T -= 1 

elif Mi == Mf:
    Tm = 0

if T >= 24 and Tm > 0:
    T = 0
    
print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)". format(T,Tm))
