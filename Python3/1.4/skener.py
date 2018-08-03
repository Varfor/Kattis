a, b, c, d = [int(x) for x in input().split()]
for i in range(a):
	indata = input()
	for x in indata:
		ut = "".join([x*d for x in indata])
	for x in range(c):
		print(ut)