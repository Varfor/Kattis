n = int(input())
bit1 = input()
bit2 = input()
for i, j in enumerate(bit1):
    if n%2==0:
        if bit1[i] != bit2[i]:
            print('Deletion failed')
            exit()
    else:
        if bit1[i] == bit2[i]:
            print('Deletion failed')
            exit()
print('Deletion succeeded')
