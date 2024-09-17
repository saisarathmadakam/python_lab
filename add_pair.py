def add_pair(d,key,value):

	if  key not in d:
		d[key]=value
	return d
	
my_dict = {'name':'sarath','age':24}
new_key=input("enter the key")
new_value=input("enter the value")
my_dict=add_pair(my_dict,new_key,new_value)

print("updated dict:",my_dict)
	
