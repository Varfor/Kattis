m = []
s = []
for _ in range(int(input())):
    a, b = [int(x) for x in input().split()]
    m.append(a*60)
    s.append(b)
slminute = sum(s)/sum(m)
if slminute<=1:
    print('measurement error')
else:
    print(slminute)
