n = []
c = []
for x in range(int(input())):
	a, b = [x for x in input().split()]
	if (a.isdigit()):
		n.append(int(a)/2)
		c.append(b)
	else:
		n.append(float(b))
		c.append(a)
ut = sorted(list(zip(n, c)))
for i in ut:
	print(i[1])