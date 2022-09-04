ABC = input().split()

a = int(ABC[0])
b = int(ABC[1])
c = int(ABC[2])

y = (a+b+abs(a-b))/2

Mbc = (y+c+abs(y-c))/2

print(int(Mbc), "eh o maior")
