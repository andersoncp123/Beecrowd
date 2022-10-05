dia = input().split()

Dia = dia[0]
DiaD = int(dia[1])

diaH = input().split(":")

H = int(diaH[0])
M = int(diaH[1])
S = int(diaH[2])

dia2 = input().split()

Dia2 = dia2[0]
DiaD2 = int(dia2[1])

diaH2 = input().split(":")

H2 = int(diaH2[0])
M2 = int(diaH2[1])
S2 = int(diaH2[2])

d = DiaD2 - DiaD
h = H2 - H
m = M2 - M
s = S2 - S

if s < 0:
	s+=60
	m-=1

if m < 0:
    m += 60
    h -= 1

if h < 0:
	h+=24
	d-=1

print("{} dia(s)". format(d))
print("{} hora(s)". format(h))
print("{} minuto(s)". format(m))
print("{} segundo(s)". format(s))
