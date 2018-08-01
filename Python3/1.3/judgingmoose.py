a, b = [int(x) for x in input().split()]
if(a+b==0):
	print("Not a moose")
else:
	print("Even %d" % (max(a,b)*2) if abs(a-b)==0 else "Odd %d" % (max(a,b)*2))