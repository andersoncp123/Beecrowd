t = int(input())

for i in range(t):
    ent = input().split()

    a = ent[0]
    b = ent[1]

    if a == b:
        print("Caso #{}: De novo!".format(i+1))

    elif a == "tesoura" and b == "papel":
        print("Caso #{}: Bazinga!".format(i+1))

    elif a == "papel" and b == "pedra":
        print("Caso #{}: Bazinga!".format(i + 1))

    elif a == "pedra" and b == "lagarto":
        print("Caso #{}: Bazinga!".format(i + 1))

    elif a == "lagarto" and b == "Spock":
        print("Caso #{}: Bazinga!".format(i + 1))

    elif a == "Spock" and b == "tesoura":
        print("Caso #{}: Bazinga!".format(i + 1))

    elif a == "tesoura" and b == "lagarto":
        print("Caso #{}: Bazinga!".format(i + 1))

    elif a == "lagarto" and b == "papel":
        print("Caso #{}: Bazinga!".format(i + 1))

    elif a == "papel" and b == "Spock":
        print("Caso #{}: Bazinga!".format(i + 1))

    elif a == "Spock" and b == "pedra":
        print("Caso #{}: Bazinga!".format(i + 1))

    elif a == "pedra" and b == "tesoura":
        print("Caso #{}: Bazinga!".format(i + 1))

    else:
        print("Caso #{}: Raj trapaceou!".format(i + 1))
