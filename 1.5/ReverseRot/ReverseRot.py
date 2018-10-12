x = dict(zip(range(28), "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."))
y = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ_.", range(28)))
a = [x for x in input().split()]
while(int(a[0])>0):
	beta = dict(zip(a[1], range(len(a[1]))))
	ut = ""
	for i in a[1]:
		ut += x[(y[i]+int(a[0]))%28]
	print(ut[::-1])	
	a = [x for x in input().split()]