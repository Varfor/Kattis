n = int(input())
while n>0:
    temp = 0
    total = 0
    for i in range(n):
        dist, time = [int(x) for x in input().split()]
        total = total+dist*(time-temp)
        temp = time
    print(total,"miles")
    n = int(input())