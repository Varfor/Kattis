a, b, c, d = [int(x) for x in input().split()]
ut = []
for i in range(a):
	indata = input()
	for x in range(c):
		ut.append("".join([x*d for x in indata]))
for i, c in enumerate(ut):
	print(''.join(ut[i]))