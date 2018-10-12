for _ in range(int(input())):
	a, b = [int(x) for x in input().split()]
	print(a, int(b*(b+1)/2), b**2, b*(b+1))