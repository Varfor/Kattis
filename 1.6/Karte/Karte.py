import re
kort = {'P': 0, 'K': 0, 'H': 0, 'T': 0}
karte = set()
for i in re.findall(r'\D\d\d', input()):
    if i not in karte:
        karte.add(i)
        kort[i[:1]] += 1
    else:
        print('GRESKA')
        exit()
for key in kort:
    print(13-kort[key], end=' ')
