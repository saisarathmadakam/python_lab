def fib(n):
	if n <=1:
		return 1
	else :
		return (fib(n-1)+fib(n-2))
a=int(input("terms"))
if a<=0:
	print("no negative numbers")
else:
	print("faboncci sequence")
	for i in range(a):
		print(fib(i)) 
