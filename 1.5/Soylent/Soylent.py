import math
cases = int(input())
for x in range(cases):
	S = int(input())
	print(math.floor(S / 400) if S % 400 == 0 else math.ceil((S / 400)))