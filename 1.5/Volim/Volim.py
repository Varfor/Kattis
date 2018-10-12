k = int(input())
person = dict(zip(range(8), "81234567"))
tid = 0
for _ in range(int(input())):
	a, b = [x for x in input().split()]
	if(tid+int(a)<210):
		if(b=="T"):
			k+=1
		tid+=int(a)
print(person[k%8])