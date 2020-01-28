
def alphabet_position(X):
	ans = ""
	for x in X:
		xInt = ord(x)
		if 97 <= xInt and xInt <= 122: 
			xInt = xInt-96
			ans += str(xInt)+' '
		elif 65 <= xInt and xInt <= 90: 
			xInt = xInt-64
			ans += str(xInt)+' '
	return ans.strip()

# import datetime
# time = 100000
# total = 0
# for index in range(time):
# 	a = datetime.datetime.now()
# 	alphabet_position("I ate dinner.")
# 	b = datetime.datetime.now()
# 	total += (b-a).microseconds
# print(total/time)

# a = input("input hear : ")
# print(a)