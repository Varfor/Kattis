price = [int(x) for x in input().split()]
arrive = []
depart = []
bil = 0
ut = 0
for _ in range(3):
    a, b = [int(x) for x in input().split()]
    arrive.append(a)
    depart.append(b)
arrive = sorted(arrive)
depart = sorted(depart)
prev = min(arrive)
for x in range(min(arrive), max(depart)+1):
    if bil>=0:
        if min(arrive) == x:
            continue
        elif x in arrive or x in depart:
            ut += (abs(x-prev))*price[bil]*(bil+1)
            bil += arrive.count(x)-depart.count(x)
            prev = x
    elif bil==-1 and x in arrive:
        bil += arrive.count(x)-depart.count(x)
        prev = x
print(ut)
