a, b = [float(x) for x in input().split()]
for i in range(int(min(a, b)), int(max(a, b)+1)):
	print (i+1)