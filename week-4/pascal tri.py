n=5
for i in range(1,n+1):
	print(" "*(n-i),end=" ")
	x=1
	for j in range(1,i+1):
		print(x,end=" ")
		x=x*(i-j)//j
	print(" ")	
