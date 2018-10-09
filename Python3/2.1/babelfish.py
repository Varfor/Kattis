import sys
d = {}
a = input()
while a != '':
    b = a.split()
    d[b[1]] = b[0]
    a = input()
for line in sys.stdin:
    if line.strip() in d:
        print(d[line.strip()])
    else:
        print('eh')
