n = int(input())
con = 1
while(con <= n):
    ent = input().split()
    a = float(ent[0])
    b = float(ent[1])
    c = float(ent[2])
    media = (a * 2 + b * 3 + c * 5) / 10
    print("{:.1f}".format(media))
    con = con + 1
