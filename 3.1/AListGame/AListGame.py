indata = int(input())
ut = 0
i = 1
while (i*i<=indata):
	if (indata%i==0):
		indata /= i
		ut +=1
		i =1
	i+=1
print(ut)