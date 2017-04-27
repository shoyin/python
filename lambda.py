

f = lambda x:x*x

f(5)

def build(x,y):
	return lambda:x*x+y*y

l =   build(2,2)

print l()