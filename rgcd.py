import math
def gcd(a,b):
	if b==0:
		return a
	else:
		return gcd(b,a%b)
n1=int(input("enter the first number"))
n2=int(input("enter the second number"))
print(gcd(n1,n2))
print(math.gcd(n1,n2))
