import datetime

def run(howmany, _function):
	total = 0
	howmany = howmany
	for _ in range(howmany):
		time_start = datetime.datetime.now()
		_function()
		time_end = datetime.datetime.now()
		total += (time_end-time_start).microseconds
	return total/howmany
