juice = [int(x) for x in input().split()]
ratio = [int(x) for x in input().split()]
part = min(juice[0]/ratio[0], juice[1]/ratio[1], juice[2]/ratio[2])
print(juice[0] - part*ratio[0], juice[1] - part*ratio[1], juice[2] - part*ratio[2])
