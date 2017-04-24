
def my_func(x):
	if x > 0:
		return 1
	else:
		return 0

name = my_func(10)
print name

def my_def(x):
	if not isinstance(x,(int,float)):
		raise TypeError('bad')
	if x > 0:
		return x
	else:
		return -x
#test = my_def('xxx')

test1 = my_def(50)
print test1