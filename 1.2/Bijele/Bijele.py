korrekt = [1,1,2,2,2,8]
bijele = [int(x) for x in input().split()]
ut = []
for i in range(len(korrekt)):
	ut.append(korrekt[i]-bijele[i])
for x in ut:
    print(x, end=" ")