#worst code ever, men den funkar.
indata = input()
t = int()
c = int()
g = int()
rutten = int()
for x in indata:
	if (x == "T"):
		t+=1
	elif(x == "C"):
		c+=1
	else:
		g+=1

if( (t>0) and (c>0) and (g>0) ):
	rutten=min(t,c,g)
print((t**2)+(c**2)+(g**2)+rutten*7)