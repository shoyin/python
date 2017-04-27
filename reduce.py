from functools import reduce

def add(x,y):
	return x + y

l = reduce(add,[1,2,3,4,5,6])
print l

def fn(x,y):
	return x * 10 + y

def char2num(s):
 	return {"0":0,"1":1,"2":2,"3":3}[s]

L = reduce(fn,map(char2num,'123'))
print L 	


def str2int(s):
	def fn(x,y):
		return x * 10 + y

	def char2num(s):
 		return {"0":0,"1":1,"2":2,"3":3}[s]
 	return reduce(fn,map(char2num,s))

s = str2int('12')
print s