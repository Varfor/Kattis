listan = [int(x) for x in input().split()]
listan.sort()
print(min(listan[0],listan[3])*max(listan[1], listan[2]))