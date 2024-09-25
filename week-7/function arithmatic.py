def add(a,b):
	return a+b
def sub(a,b):
	return a-b
def multi(a,b):
	return a*b
def div(a,b):
	return a/b
n1=float(input("enter the first num"))
n2=float(input("enter the first num"))
operation=(input("choose operation (+,-,*,/):"))
if operation == "+":
	print("result=:",add(n1,n2))
elif operation == "-":
	print("result=:",sub(n1,n2))
elif operation == "*":
	print("result=:",multi(n1,n2))
elif operation == "/":
	print("result=:",div(n1,n2))
else:
	print("invalid operator")

	 
