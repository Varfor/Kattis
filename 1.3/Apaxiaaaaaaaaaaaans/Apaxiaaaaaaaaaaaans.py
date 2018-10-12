name = input()
ut = ""
for c in name:
	if(c not in ut[-1:]):
		ut += c
print(ut)