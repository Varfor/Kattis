cases = int(input())
while cases > 0:
    a = []
    b = []
    for i in range(cases):
        a.append(int(input()))
        pass
    for i in range(cases):
        b.append(int(input()))
        pass
    c = dict(zip(sorted(a),sorted(b)))
    for items in a:
        print(c[items])
    print()
    cases = int(input())
