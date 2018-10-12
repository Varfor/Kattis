input()
y = 0
temp = [int(x) for x in input().split()]
for i, x in enumerate(temp):
	if(temp[i]<0):
		y+=1
print(y)