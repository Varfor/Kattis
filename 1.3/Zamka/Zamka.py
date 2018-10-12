l = int(input())
d = int(input())
x = int(input())
utmin = int()
utmax = int()
for i in range(l, d+1):
	if(sum([int(x) for x in str(i)]) == x):
		utmin = i
		break
for i in range(d, l-1, -1):
	if(sum([int(x) for x in str(i)]) == x):
		utmax = i
		break
print(utmin)
print(utmax)