def validate_pin(x):
	if len(x) != 4 and len(x) != 6: 
		return False
	try:
		if(x<0): return False
		int(x)
		return True
	except:
		return False

# def validate_pin(x):
	# import re
	# return bool(re.search('([0-9]{4})|([0-9]{6})',x))
	# return bool(re.search('^.{0,4}$',x))
	# return bool(re.search(r'\d+', '5Need47forSpeed 2'))

# def x():
# 	validate_pin('AA')

# import timeit
# print(timeit.timeit(x,number=1000000))
# import TimeTester

# print(TimeTester.run(1000000,x))

# print(validate_pin('-100'))