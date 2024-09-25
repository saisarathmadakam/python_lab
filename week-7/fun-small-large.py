def fun(a):
 	max=min=a[0]
 	for i in a[1:]:
 		if i>max:
 			max=i
 		if i<min:
 			min=i
 	return max,min
a=(2,3,4,5,6)
print(fun(a))
