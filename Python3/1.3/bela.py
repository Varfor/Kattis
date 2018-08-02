card = ["A", "K", "Q", "J", "T", "9", "8", "7"]
pointsd = [11, 4, 3, 20, 10, 14, 0, 0]
pointsnd = [11, 4, 3, 2, 10 ,0 ,0 ,0]
dominant = dict(zip(card,pointsd))
nondominant = dict(zip(card,pointsnd))
total = int()
hands, suit = [x for x in input().split()]
for i in range(int(hands)*4):
	c, s = [x for x in input()]
	if (s == suit):
		total += int(dominant[c])
	else:
		total += int(nondominant[c])
print(total)