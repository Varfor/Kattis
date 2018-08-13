a, b = [int(x) for x in input().split()]
grid = []
newgrid = []
for i in range(a):
    o = input()
    grid.append(o)
k = ""
for j in grid:
    for c in j:
        if(c=='#'):
            if(len(k)>=2): newgrid.append(k)
            k = ""
            continue
        else:
            k += c
    if(len(k)>=2): newgrid.append(k)
    k = ""
for i in range(b):
    d = ""
    for j in grid:
        if(j[i] == '#'):
            if(len(d)>=2): newgrid.append(d)
            d = ""
            continue
        else:
            d += j[i]
    if(len(d)>=2): newgrid.append(d)
print(sorted(newgrid)[0])
