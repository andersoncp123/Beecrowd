a, b, c = map(int, input().split())

if a > b <= c:
    print(":)")

elif a < b >= c:
    print(":(")

elif a < b < c and (c - b) < (b - a):
    print(":(")

elif a < b < c and (c - b) >= (b - a):
    print(":)")

elif a > b > c and (b - c) < (a - b):
    print(":)")

elif a > b > c and (b - c) >= (a - b):
    print(":(")

elif a == b > c:
    print(":(")

elif a == b < c:
    print(":)")

elif a == b == c:
    print(":(")
