n = int(input())
batter = [int(x) for x in input().split()]
for i in range(len(batter)):
	if(batter[i]<0):
		batter[i] = 0
		n-=1
print(sum(batter)/n)