def log(fun):
	def wrapper(*args,**kw):
		print('call %s() :' % fun.__name__)
		return fun(*args,**kw)
	return wrapper
	
@log
def now():
	print 11111

now()			