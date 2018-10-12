import math
ignore = input()
r = [int(x) for x in input().split()]
for element in r[1:]:
    a = r[0]
    b = element
    gcd = math.gcd(a,b)
    print('%d/%d' %(a/gcd, b/gcd))
