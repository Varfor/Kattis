n = int(input())
i = 11
while True:
	if (n == 0):
		break
	if(sum([int(x) for x in str(n)]) == sum([int(x) for x in str(n*i)])):
		print(i)
		i = 11
		n = int(input())
	else:
		i+=1