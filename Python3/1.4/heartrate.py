for i in range(int(input())):
	b, p = [float(x) for x in input().split()]
	c = 60/p
	abpm = b*60/p
	print("{:.4f}".format(abpm-c), "{:.4f}".format(abpm), "{:.4f}".format(abpm+c))