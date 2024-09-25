l=[]
n=int(input("enter the elements"))
for i in range(n):
	ele=int(input())
	l.append(ele)
print(l)
min_num=l.index(min(l))
max_num=l.index(max(l))
print(max_num)
print(min_num)	
