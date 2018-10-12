x = 0;
for i in range(int(input())):
	p = int(input())
	x = x+(((p-(p%10))/10)**(p%10))
print(int(x))