def fun(a):
 	first=second=a[0]
 	for i in a[1:]:
 		if i>first:
 			second=first
 			first=i
 		if second<i<first:
 			second=i
 	return second
a=(2,3,4,5,6)
print(fun(a))
