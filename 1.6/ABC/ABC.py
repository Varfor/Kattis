lista = input().split()
listan = []
for i in lista: listan.append(int(i))
listan.sort()
for i, char in enumerate(input().lower()):
	print(listan[ord(char) - 97], end=" ")