l=[]
n=int(input("enter the elements"))
for i in range(n):
	ele=int(input())
	l.append(ele)
print(l)	
s=sum(l)
avg=s/len(l)
print(s)
print(avg)	
