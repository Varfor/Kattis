Gunnar = g1, g2, g3, g4 = [int(x) for x in input().split()]
Emma = e1, e2, e3, e4 = [int(x) for x in input().split()]
if (sum(Emma)/4>sum(Gunnar)/4):
	print("Emma")
elif (sum(Emma)/4<sum(Gunnar)/4):
	print("Gunnar")
else:
	print("Tie")