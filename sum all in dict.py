def sum_val(d):
	if not d:
		return 0
	key,value = d.popitem()
	
	return value + sum_val(d)
	
my_dict = { 1:20,2:30}
total=sum_val(my_dict.copy())
print(total)
