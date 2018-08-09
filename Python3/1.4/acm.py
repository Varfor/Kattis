test = []
total = 0
right = 0
a = [x for x in input().split()]
while(int(a[0])>=0):
	if(a[2] == "right"):
		right+=1
		total+=int(a[0])
		if(a[1] in test):
			total+=20*test.count(a[1])
	else:
		test.append(a[1])
	a = [x for x in input().split()]
print(right, total)