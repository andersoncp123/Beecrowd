num = list(map(int,input().strip().split()))

if num[0] != num[1]:
    num.sort()
    print(num[1])

if num[0] == num[1]:
    print(num[1])
