n=int(input("enter the number"))
char=65
for i in range(1,n+1):
	for j in range(1,i+1):
		print(chr(char),end=" ")
	char+=1
	print(" ")		
