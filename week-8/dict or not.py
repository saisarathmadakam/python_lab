my_dict={'name':'sarath','age':25}

def check_key(d,key):
	if key in d:
		return True
	return False
key=input("enter the key")
if check_key(my_dict,key):
	print("key exits")
else:
	print("does not exits")	
