n, p, q = [int(x) for x in input().split()]
p += q
print('paul' if (p/n)%2==0 else 'opponent')
