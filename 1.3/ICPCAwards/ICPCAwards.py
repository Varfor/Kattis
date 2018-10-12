skola = []
grupp = set()
for i in range(int(input())):
	a, b = [x for x in input().split()]
	if (a not in grupp):
		grupp.add(a)
		skola.append(a+" "+b)
for i in skola[:12]:
		print(i)