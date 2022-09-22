valores = input(). split()

a = int(valores[0])
b = int(valores[1])

if b % a == 0 or a % b == 0: 
    print("Sao Multiplos")
    
else:
    print("Nao sao Multiplos")
