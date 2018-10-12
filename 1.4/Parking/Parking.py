for i in range(int(input())):
	input()#rör ej
	listan = [int(x) for x in input().split()]
	print( (max(listan)-min(listan)) *2 )