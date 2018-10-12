p, d = [int(x) for x in input().split()]
boatitems = set()
for i in range(d):
    boatitems.add(input())
    if len(boatitems)==p:
        print(i+1)
        exit()
print('paradox avoided')
