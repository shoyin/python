d = {'x':1,'b':2,'d':3}

for x in d:
	print d[x]

for key,value in enumerate(d):
	print(key)


for x,y in[(1,1),(2,3)]:
	print (x,y)

it = iter([1,2,3,4,5])

print next(it)
print next(it)
print next(it)
print next(it)
for k, v in d.items():
	print (k,v)