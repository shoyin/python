import functools

def log(test):

	if isinstance(test,str):
		def decorator(func):
			@functools.wraps(func)
			def wrapper(*arg,**kw):
				print 111111111
				func(*arg,**kw)
				print 2222222222
			return wrapper
		return decorator	

	else:
		@functools.wraps(test)
		def wrapper(*arg,**kw):
			print 111111111
			test(*arg,**kw)
			print 444444
		return wrapper

@log
def now():
    print('2017-4-25')

now()

@log('execute')
def now():
    print('2017-4-25')


now()
