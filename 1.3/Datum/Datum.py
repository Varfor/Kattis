from datetime import date
d, m = [int(x) for x in input().split()]
print(date(2009, m, d).strftime("%A"))