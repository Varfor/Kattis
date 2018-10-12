a, b = [int(x) for x in input().split()]
while (a+b>0):
    if (a+b==13):
        print('Never speak again.')
    elif (a<b):
        print('Left beehind.')
    elif (a>b):
        print('To the convention.')
    else:
        print('Undecided.')
    a, b = [int(x) for x in input().split()]
