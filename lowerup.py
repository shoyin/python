def fn(s):
	return s[0].upper() + s[1:].lower()

L1 = ['adam', 'LISA', 'barT']

L2 = list(map(fn,L1))

print L2


def prod(L):
 	
	def sum(x,y):
		return x * y

	return reduce(sum,L)	
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))	