for i in range(int(input())):
    a, b, c, d = [x for x in input().split()]
    print(a, end = " ")
    if (int(b[:4])>=2010 or int(c[:4])>=1991):
        print('eligible')
    elif int(d)>=41:
        print('ineligible')
    else:
        print('coach petitions')
