price = [int(x) for x in input().split()]
arrive = []
depart = []
bil = -1
ut = 0
for _ in range(3):
    a, b = [int(x) for x in input().split()]
    arrive.append(a)
    depart.append(b)
prev = min(arrive)
for x in range(min(arrive), max(depart)):
    if x in arrive or x in depart:
        bil += arrive.count(x)-depart.count(x)
        print(ut, bil)
        prev = x
        print('value:', x,'price[bil]:', price[bil])
    if:
        ut += abs(x-prev)*price[bil]
        # print(arrive.count(x), depart.count(x), price[bil])
print(ut)
