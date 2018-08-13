y = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ '", range(28)))
banan = int()
steps = 0
for _ in range(int(input())):
    indata = input().upper()
    pos1 = y[indata[:1]]
    for a in indata[1:]:
        pos2 = y[a]
        steps += min( abs(pos1-pos2), 28-abs(pos1-pos2) )
        pos1 = y[a]
    print(steps*0.4487989505119047619047619047619+len(indata))
    steps = 0
