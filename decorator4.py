import functools
def log(text):
	if isinstance(text,str):
		def decorator(func):
			@functools.wraps(func)
			def wrapper(*args,**kw):
				print("%s %s"%(text,func.__name__))
				func(*args,**kw)
			return wrapper
		return decorator

	else:

		@functools.wraps(text)
		def wrapper(*args,**kw):
			print(" %s"%(text.__name__))
			text(*args,**kw)
		return wrapper

@log
def now():
	print 11111


@log('execute')
def now():
    print('2017-4-25')

now()
