for _ in range(int(input())):
    a = input()[::-1]
    ut = []
    for j, i in enumerate([int(x) for x in a]):
        if j%2!=0:
            i *= 2
            if i>9:
                i -= 9
        ut.append(i)
    print('PASS' if sum(ut)%10==0 else 'FAIL')
