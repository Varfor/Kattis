p, q, s = [int(x) for x in input().split()]
set1 = set()
set2 = set()
a = 0
while a+p<=s:
    a += p
    set1.add(a)
a = 0
while a+q<=s:
    a += q
    set2.add(a)
print('yes' if any(set1.intersection(set2)) else 'no')
