for i in range(int(input())):
	listan = [int(x) for x in input().split()]
	if(listan[0]+listan[1]==listan[2]):
		print("Possible")
	elif(abs(listan[0]-listan[1])==listan[2]):
		print("Possible")
	elif(listan[0]/listan[1]==listan[2]):
		print("Possible")
	elif(listan[0]*listan[1]==listan[2]):
		print("Possible")
	elif(listan[1]/listan[0]==listan[2]):
		print("Possible")
	else:
		print("Impossible")