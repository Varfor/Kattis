import math
D, V = [int(x) for x in input().split()]
while(D+V>0):
	print( (((-6*V)/math.pi)+D**3)**(1/3) )
	D, V = [int(x) for x in input().split()]