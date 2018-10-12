a = int(input())
aset = 0
uppner = True
upp = []
ner = []
while(a>0):
	for _ in range(a):
		if(uppner):
			upp.append(input())
		else:
			ner.append(input())
		uppner = not uppner
	aset+=1
	print("SET", aset)
	for i in upp:
		print(i)
	for i in reversed(ner):
		print(i)
	upp.clear()
	ner.clear()
	uppner = True
	a = int(input())