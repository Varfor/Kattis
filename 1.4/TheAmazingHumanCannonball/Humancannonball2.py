import math
g = 9.81
for i in range(int(input())):
	velocity, angle, x, h1, h2 = [float(x) for x in input().split()]
	time = x/(velocity*math.cos(angle*math.pi/180))
	y = velocity*time*math.sin(angle*math.pi/180)-0.5*g*time**2
	print("Safe" if (y>h1+1) and (y<h2-1)else "Not Safe")