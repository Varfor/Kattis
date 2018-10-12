for i in range(int(input())):
	n = input()
	m = input()
	o = ""
	for i in range(len(n)):
		if (n[i] == m[i]):
			o += "."
		else:
			o += "*"
	print (n)
	print (m)
	print (o, "\n")