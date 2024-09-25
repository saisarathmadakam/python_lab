import csv
f=open('sample.txt','r')
print('initial position:',f.tell())
f.seek(10)
print('position after seek:',f.tell())
print(f.read(5))
print('position after read:',f.tell())


data=[
     ['s.no','rollno','name'],
     [1,101,'saaa']
     ]
     
with open ('table.csv','w',newline='')as file:
	w=csv.writer(file)
	w.writerows(data)


data=[
     ['s.no','rollno','name'],
     [1,101,'saaa']
     ]
     
with open ('table.csv','a',newline='')as file:
	w=csv.writer(file)
	w.writerows(data)
print("data append successfully")


