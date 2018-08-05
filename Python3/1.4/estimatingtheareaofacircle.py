import math
r, m, c = [float(x) for x in input().split()]
while (r+m+c>0):
	print("{:.5f}".format(math.pi*r**2), "{:.5f}".format(4*r**2*c/m))
	r, m, c = [float(x) for x in input().split()]