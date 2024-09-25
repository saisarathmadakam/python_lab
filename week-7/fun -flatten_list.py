def flatten(a):
	flat_list=[]
	for i in a:
		for x in i:
			flat_list.append(x)
	return flat_list
a=[[1,2],[3,4]]
flat=flatten(a)
print(flat)
	
	
