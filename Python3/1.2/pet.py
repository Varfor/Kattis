listan = []
listan.append(sum(int(x) for x in input().split()))
listan.append(sum(int(x) for x in input().split()))
listan.append(sum(int(x) for x in input().split()))
listan.append(sum(int(x) for x in input().split()))
listan.append(sum(int(x) for x in input().split()))
print(list.index(listan, max(listan))+1, max(listan))