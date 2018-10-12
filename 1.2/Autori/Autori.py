autori = [x for x in input().split("-")]
ut = []
for i in range(len(autori)):
	ut.append(autori[i][:1])
for x in ut:
    print(x.upper(), end="")