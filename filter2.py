

def filters(s):

	l = str(abs(s))
	return l == l[::-1]


x = filter(filters,range(1000))
print x