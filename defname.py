def now():
	print 111

F = now

F()

print now.__name__
print F.__name__


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
	print 111

now()	
