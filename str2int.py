from functools import reduce

def str2int(s):
	def fn(x,y):
		return x * 10 + y
	def char2num(s):
		return {"0":0,"1":1,"2":2,"3":3,"4":4}[s]
	return reduce(fn,map(char2num,s))

I = str2int("012")

print I		