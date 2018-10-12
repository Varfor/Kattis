for _ in range(int(input())):
    a = [int(x) for x in input().split()[1:]]
    for nr, element in enumerate(a):
        if a[nr+1] != a[nr]+1:
            print(nr+2)
            break
