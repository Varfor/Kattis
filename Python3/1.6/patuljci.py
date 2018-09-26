a = []
for _ in range(9):
     a.append(int(input()))
for elementA in a:
    if sum(a)-elementA<100:
        continue
    else:
        for elementB in a:
            if elementA is not elementB:
                if sum(a)-elementA-elementB==100:
                    a.remove(elementA)
                    a.remove(elementB)
for i in a:
    print(i)
