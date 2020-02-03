def validate_pin(x):
	if len(x) != 4 and len(x) != 6: 
		return False
	try:
		a = int(x)
		if(a<0): return False
		return True
	except:
		return False

# import re
# def validate_pin(x):
# 	return bool(re.match('^(([0-9]{4})([0-9]{2})?)$',x))

# def validate_pin(pin):
# 	if len(pin) == 6 or len(pin) == 4:
# 		return pin.isdigit()
# 	else:
# 		return False

# import timeit
# def x():
# 	validate_pin('100x')
# print(timeit.timeit(x,number=1000000))


# def x():
# 	validate_pin('AA')

# import timeit
# print(timeit.timeit(x,number=1000000))
# import TimeTester

# print(TimeTester.run(1000000,x))

# print(validate_pin('1-11'))