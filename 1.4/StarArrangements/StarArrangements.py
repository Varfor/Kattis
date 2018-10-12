stars = int(input())
print("%d:" % (stars))
for i in range(2, stars):
	if ((stars%(i+(i-1)) == 0) or (stars%(i+(i-1)) == i)):
		print("%d,%d" % (i, i-1))
	if (stars%i==0):
		print("%d,%d" % (i, i))