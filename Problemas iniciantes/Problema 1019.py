segundos = int(input())

horas = segundos//(60*60)
segundos = segundos%(60*60)

minutos = segundos//60
segundos = segundos%60

print("{}:{}:{}". format(horas, minutos, segundos))
