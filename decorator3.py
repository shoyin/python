def log(fun):
	def wrapper(*args,**kw):
		print ("begin call")
		fun(*args,**kw)
		print ("end call")
	return wrapper

@log
def now():
	print 1

now()		