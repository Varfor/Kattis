for _ in range(int(input())):
    a = [int(x) for x in input().split()[1:]]
    avg = sum([x for x in a])/len(a)
    print('{0:.3f}%'.format(len([x for x in a if x>avg])/len(a)*100))
