import math
a, b = [int(x) for x in input().split()]
print( ((math.pi*((a-b)**2)) / (math.pi*(a**2))*100) )