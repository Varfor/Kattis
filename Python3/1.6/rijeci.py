k = int(input())
a = 1
b = 0
for i in range(k):
    c = b
    b += a
    a = c
print(a, b)
