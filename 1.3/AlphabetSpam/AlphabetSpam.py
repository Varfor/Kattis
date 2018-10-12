a = input()
b = len(a)
low =len([c for c in a if c=='_'])/b
upp = len([c for c in a if c.islower()])/b
whi =len([c for c in a if c.isupper()])/b 
sym = 1-low-upp-whi
print(low, upp, whi, sym, sep='\n')