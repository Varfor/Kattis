input() #ignoreras
adrian = ["A", "B", "C", "A", "B", "C", "A", "B", "C", "A", "B", "C"]
bruno  = ["B", "A", "B", "C", "B", "A", "B", "C", "B", "A", "B", "C"]
goran  = ["C", "C", "A", "A", "B", "B", "C", "C", "A", "A", "B", "B"]
ADR = dict(zip(range(12),adrian))
BRU = dict(zip(range(12),bruno))
GOR = dict(zip(range(12),goran))
A = int()
B = int()
G = int()
svar = input()
for i, c in enumerate(svar):
	if(c == ADR[i%12]):
		A +=1
	if(c == BRU[i%12]):
		B +=1
	if(c == GOR[i%12]):
		G +=1
count = [A,B,G]
people = ["Adrian", "Bruno", "Goran"]
print(max(count))
for i, x in enumerate(count):
	if(x == max(count)):
		print(people[i%12])