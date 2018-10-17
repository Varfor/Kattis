ut = 0
a, b = [int(x) for x in input().split()]
for i in range(a):
    ok = True
    for j in range(b):
        case = input()
        if (case[0].isupper() and case[1:].islower()) or case.islower():
            continue
        else:
            ok = False
    if ok == True:
        ut += 1
print(ut)
