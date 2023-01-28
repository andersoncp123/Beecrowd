while True:
    try:
        ent1 = float(input())
        ent2 = float(input())

        pi = 3.14
        r = ent2/2

        altura = ent1/(pi*r**2)
        areab = pi*r**2

        print("ALTURA = {:.2f}".format(altura))
        print("AREA = {:.2f}".format(areab))
    except:
        break
