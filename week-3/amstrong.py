n=int(input("enter the value:"))
sum=0
temp=n
while temp>0 :
     remainder=temp%10
     sum += remainder**3
     temp//=10
     
     
if n==sum:
     print("amstrong")
else :
     print("not amstrong")










     
