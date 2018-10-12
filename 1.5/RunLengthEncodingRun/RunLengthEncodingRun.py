a = input().split()
b = a[1]
ut = ''
count = 1
if a[0] == 'E':
    for char in b:
        if ut[-1:] == char:
            count += 1
            continue
        else:
            ut += str(count)+char
            count = 1
            continue
    ut += str(count)
    print(ut[1:])
else:
    for i, char in enumerate(b):
        if not char.isdigit():
            ut += char*int(b[i+1])
    print(ut)
