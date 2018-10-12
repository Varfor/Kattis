n = int(input())
for i in range(n):
	input()#rör ej
	listan = [int(x) for x in input().split()]
	for x in listan:
		if listan.count(x) == 1:
			print("Case #%d: %d" % (i+1, x))
			break