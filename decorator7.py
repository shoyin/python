import functools

def log(strfunc):
	if isinstance(strfunc,str):

		def decorator(func):
			@functools.wraps(func)

			def wrapper(*arg,**kw):
				
				print 111111111
				print('call %s %s' %(strfunc,func.__name__))
				func(*arg,**kw)	
			return wrapper
		return decorator		
	else:
		@functools.wraps(strfunc)
		def wrapper(*arg,**kw):	
			print 22222
			strfunc(*arg,**kw)	
		return wrapper



@log('test')
def now():
    print('2015-3-25')

now()    