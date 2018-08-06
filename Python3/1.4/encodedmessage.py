#BORROWED solution from: https://github.com/hliuliu/kattis_problems/blob/master/encodedmessage/encodedmessage.py
#used as learning experiment with lists.
for i in range(int(input())):
	indata = input()
	r = int(len(indata)**.5)
	grid = [['']*r for x in range(r)]
	for i, c in enumerate(indata):
		rad = i%r
		kol = i//r
		grid[rad][kol] = c
		#print(i//r, i%r)
		#print(grid[kol][rad])
	print(''.join([''.join(kol) for kol in grid[::-1]]))