dias = int(input())

anos = dias//365
dias = dias%365

meses = dias//30
dias = dias%30

print("{} ano(s)". format(anos))
print("{} mes(es)". format(meses))
print("{} dia(s)". format(dias))
