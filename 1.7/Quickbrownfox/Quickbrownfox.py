for _ in range(int(input())):
    a = input()
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    abc = set()
    for char in a.lower():
        if char.isalpha(): abc.add(char)
    if len(abc)>=26:
        print('pangram')
    else:
        print('missing', ''.join([x for x in alpha if x not in abc]))
