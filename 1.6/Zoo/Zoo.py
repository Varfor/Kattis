lista = 0
a = int(input())
while a>0:
    lista += 1
    djur = {}
    for _ in range(a):
        indata = input().split()[-1].lower()
        if indata in djur:
            djur[indata] += 1
        else:
            djur[indata] = 1
    print('List %d:' %lista)
    for key in (sorted(djur.keys())):
        print(key, "|", djur[key])
    a = int(input())
