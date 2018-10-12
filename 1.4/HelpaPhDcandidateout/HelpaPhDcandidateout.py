for i in range(int(input())):
	a = input()
	print("skipped" if a.upper()=="P=NP" else sum([int(x) for x in a.split("+")]))