import sys
d = {}
def kalkylera(lista):
    total = 0
    pm = True
    try:
        for i in lista:
            if i == '=':
                break
            elif i == '-':
                pm = False
                continue
            elif i == '+':
                pm = True
                continue
            if pm == True:
                total += int(d[i])
            else:
                total -= int(d[i])
        for i in d:
            if int(d[i]) == total:
                return(i)
        return('unknown')
    except:
        return('unknown')

for line in sys.stdin:
    indata = line.lower().split()
    if 'def' == indata[0]:
        d[indata[1]] = indata[2]
    elif 'calc' == indata[0]:
        print(' '.join(indata[1:]), kalkylera(indata[1:]))
    elif 'clear' == indata[0]:
        d.clear()
