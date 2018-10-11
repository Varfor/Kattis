import sys
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '..--', '.-.-', '---.', '----']
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '_', ',', '.', '?']
mtoa = dict(zip(morse, alpha))
atom = dict(zip(alpha, morse))
for line in sys.stdin:
    count = 0
    c = ''
    a = [len(atom[x]) for x in line[:-1][::-1]]
    b = ''.join([atom[x] for x in line[:-1]])
    for i in a:
        c += mtoa[b[count:i+count]]
        count += int(i)
    print(c)
