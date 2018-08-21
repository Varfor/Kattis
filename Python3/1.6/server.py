a, b = [int(x) for x in input().split()]
x = [int(x) for x in input().split()]
ut = 0
for i in x:
    if(b - i < 0):
        break
    else:
        ut += 1
        b  -= i
print(ut)
