s = 0
count = 0

while count < 3:
    ent = input()

    if ent != "caw caw":
        if ent == "---":
            s += 0

        elif ent == "--*":
            s += 1

        elif ent == "-*-":
            s += 2

        elif ent == "*--":
            s += 4

        elif ent == "-**":
            s += 3

        elif ent == "**-":
            s += 6

        elif ent == "***":
            s += 7

        elif ent == "*-*":
            s += 5

    else:
        print(s)
        s = 0
        count += 1
