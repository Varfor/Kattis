ignore = input()
a = [x for x in input().split()]
for i, j in enumerate(a):
    if j == 'mumble':
        continue
    elif int(j) == i+1:
        continue
    else:
        print('something is fishy')
        exit()
print('makes sense')
