notas = input(). split()

n1 = float(notas[0])
n2 = float(notas[1])
n3 = float(notas[2])
n4 = float(notas[3])

N1 = n1*2
N2 = n2*3
N3 = n3*4
N4 = n4*1

media = (N1+N2+N3+N4)/10
print("Media: {:.1f}". format(media))

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
elif 5.0 <= media <= 6.9:
    print("Aluno em exame.")
    exam = float(input())
    print("Nota do exame: {:.1f}". format(exam))
    MNova = (media + exam)/2
    if MNova >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: {:.1f}". format(MNova))
