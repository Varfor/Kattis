a, b, c = [int(x) for x in input().split()]
a += b
ut = 0
while a >= c:
    ut += a//c
    a = a%c + a//c
print(ut)
