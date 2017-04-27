print sorted([1,2,55,555,55,555,55555])

print sorted([1,2,-55,555,55,555,55555],key=abs)

print sorted(['xxxxxxxxxxxxx','b','AAAAA'],key = str.lower,reverse = True)


def by_name(t):
	return t[0]


def by_score(t):
	return t[1]

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
s = sorted(L,key=by_name)
print s

l = sorted(L,key = by_score)
print l