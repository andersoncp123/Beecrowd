n = int(input())

for i in range(n):
    a,b,c,d = map(str,input().strip().split(" "))

    num1,num2 = map(int,input().strip().split())

    if (num1 + num2) % 2 == 0:
        if b == "PAR":
            print(a)
        else:
            print(c)

    else:
        if b == "IMPAR":
            print(a)
        else:
            print(c)
