d = {}
for _ in range(int(input())):
    a, b = [x for x in input().split()]
    if b in d:
        if d[b] == a:
            print('%s entered (ANOMALY)' %(b) if a == 'entry' else '%s exited (ANOMALY)' %(b))
        else:
            d[b] = a
            print('%s entered' %(b) if a == 'entry' else '%s exited' %(b))
    else:
        d[b] = a
        if a == 'entry':
            print('%s entered' %(b))
        else:
             print('%s exited (ANOMALY)' %(b))
