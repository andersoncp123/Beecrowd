num = float(input())

if num == 0:
    if len(str(num)) > 3:
        print("-0.0000E+00")
    else:
        print("+0.0000E+00")

elif num > 0:
    print("+{:.4E}". format(num))

else:
    print("{:.4E}". format(num))
