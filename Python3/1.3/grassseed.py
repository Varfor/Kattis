c = float(input())
total = float()
for i in range(int(input())):
	a, b = [float(x) for x in input().split()]
	total = total+a*b
print(total*c)