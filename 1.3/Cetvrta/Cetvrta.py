x = []
y = []
for i in range(3):
	a, b = [int(x) for x in input().split()]
	x.append(a)
	y.append(b)
print(*[i for i in x if x.count(i)==1], *[i for i in y if y.count(i)==1])