n, m = [int(x) for x in input().split()]
if abs(n-m) == 1:
    if n<m:
        print('Dr. Chaz will have 1 piece of chicken left over!')
    else:
        print('Dr. Chaz needs 1 more piece of chicken!')
else:
    if n<m:
        print('Dr. Chaz will have %d pieces of chicken left over!' %abs(n-m))
    else:
        print('Dr. Chaz needs %d more pieces of chicken!' %abs(n-m))
