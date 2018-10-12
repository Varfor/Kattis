import math
h,v = [int(x) for x in input().split()]
print(math.ceil((h) / math.sin(math.radians(v))))