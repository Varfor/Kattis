for x in range(int(input())):
	born = -1
	turtle = [int(x) for x in input().split()]
	for i, c in enumerate(turtle[:-1]):
		if( c>turtle[i-1]*2 ):
			born += c-turtle[i-1]*2
	print(born)