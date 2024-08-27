def gcd(a,b):
	while(b!=0):
		a,b=b,a%b
	return a
n1=int(input("enter the first num"))
n2=int(input("enter the second num"))

result=gcd(n1,n2)

print(result)
	
