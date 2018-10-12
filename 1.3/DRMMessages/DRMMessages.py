drm = input()
drmhalf = int(len(drm)/2)
ut1 = []
ut2 = []
temp1 = []
temp2 = []
for i in drm[:drmhalf]:
	ut1.append(ord(i)-65)
for i in drm[drmhalf:]:
	ut2.append(ord(i)-65)
for i in ut1:
	temp1.append((((i)+sum(ut1))%26)+65)
for i in ut2:
	temp2.append((((i)+sum(ut2))%26)+65)
for i, x in enumerate(temp1):
	print(chr(((x)+temp2[i])%26+65), end="")
#dummaste programmet, skriv med en mappad lista sen