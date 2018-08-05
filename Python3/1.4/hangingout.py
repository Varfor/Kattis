a, b = [int(x) for x in input().split()]
ut = 0
p = 0
for i in range(b):
	c, d = [x for x in input().split()]
	if(c == "enter"):
		if(p+int(d)<=a):
			p+=int(d)
		else:
			ut+=1
	else:
		if(p-int(d)>=0):
			p-=int(d)
print(ut)