l=[]
n=int(input("enter the elements"))
for i in range(n):
	ele=int(input())
	l.append(ele)
print(l)
eleremove=30
if eleremove in l:	
	l.remove(eleremove)
print(l)
