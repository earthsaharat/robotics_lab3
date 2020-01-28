def validate_pin(x):
	if len(x) != 4 and len(x) != 6: 
		return False
	try:
		int(x)
		return True
	except:
		return False

# print(validate_pin('0123a'))