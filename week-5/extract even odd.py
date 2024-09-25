l=[]
n=int(input("enter the elements"))
for i in range(n):
	ele=int(input())
	l.append(ele)
print(l)
even=[]
odd=[]
for ele in l:
	if ele%2==0:
   		even.append(ele)
	else:
   		odd.append(ele)
print(even)
print(odd)			
