for x in range(int(input())):
    a, b = [int(x) for x in input().split()]
    grid = []
    for _ in range(a):
        grid.append(input())
    print('Test', x+1)
    for i in grid[::-1]:
        print(i[::-1])
