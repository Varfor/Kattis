while True:
    try:
        a = [x for x in input().split()]
        b = [float(x) for x in a if not x.isalpha()]
        c = [x for x in a if x.isalpha()]
        print(sum(b)/len(b), ' '.join(str(x) for x in c))
    except:
        exit()
