list = [x*x for x in xrange(1,10)]

print list


list = [m + n for m in xrange(1,10) for n in xrange(1,10)]
print list



L1 = ['Hello', 'World', 18, 'Apple', None]

L2 = [x.lower() for x in L1 if isinstance(x,str)]

print L2