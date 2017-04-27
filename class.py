class Student(object):
	def __init__(self,name,score):
		self.__name = name
		self.__score = score

	def get_name(self):
		return self.__name

bart = Student('Bart Simpson', 98)

print bart.get_name()

bart.__name = 'xxxxx'

print bart.__name

print bart.get_name()

print bart._Student__name
