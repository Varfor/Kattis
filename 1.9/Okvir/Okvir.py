x, y = [int(x) for x in input().split()]
u, l, r, d = [int(x) for x in input().split()]
words = []
for _ in range(x):
    words.append(input())
ut = []
for i in range(u+d+x):
    data = ''
    for j in range(l+r+y):
        if (i+j)%2==0:
            data += '#'
        else:
            data += '.'
    ut.append(data)
for j, i in enumerate(range(u, u+x)):
    ut[i] = ''.join(ut[i][:l]) + words[j] + ''.join(ut[i][l+y:])
print('\n'.join(ut))
