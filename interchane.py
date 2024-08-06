l=[]
n=int(input("enter the elements"))
for i in range(n):
	ele=int(input())
	l.append(ele)
print(l)
l[0],l[-1]=l[-1],l[0]
print(l)




	
