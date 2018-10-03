a = [x for x in input().split()]
ut = 0
for element in a:
    if 'ae' in element.lower():
        ut +=1
if ut/len(a)>=.40:
    print('dae ae ju traeligt va')
else:
    print('haer talar vi rikssvenska')
