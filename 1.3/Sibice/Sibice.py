import math
cases, width, height = [int(x) for x in input().split()]
boxSize = float(((width**2)+(height**2))**0.5)
for i in range(cases):
    print("DA" if int(input()) <= boxSize else "NE")