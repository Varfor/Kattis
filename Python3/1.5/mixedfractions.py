a, b = [int(x) for x in input().split()]
while a+b>0:
    print(a//b, a%b, "/", b)
    a, b = [int(x) for x in input().split()]
