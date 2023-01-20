ent = list(map(float,input().split()))

porcentagem = (ent[1] - ent[0]) / ent[0] * 100

print("{:.2f}%". format(porcentagem))
