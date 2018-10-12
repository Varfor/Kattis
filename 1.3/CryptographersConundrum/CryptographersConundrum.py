per = "PER"
cipher = input().upper()
count = int()
for i, c in enumerate(cipher):
	if (c not in per[i%3]):
		count += 1
print(count)