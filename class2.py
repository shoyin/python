class Animal(object):
	def run(self):
		print ("Animal runing")

class Dog(Animal):
	def run(self):
		print ("dpg runing")

d = Dog()

d.run()


def run_twice(animal):
	animal.run()
	animal.run()


run_twice(d)
