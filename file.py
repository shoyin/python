f = open('F:/python/test.txt', 'r')
l=f.read()
print l

f.close()


with open('F:/python/test.txt', 'w') as f:
	print f.write('xxxxxx')

with open('F:/python/test.txt', 'r') as f:
	print f.read()


