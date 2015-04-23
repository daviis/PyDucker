class Animal():
	def __init__(self, idNum):
		"""
		@idNum:int
		"""
		id = idNum
		
	def speak(self):
		print("i dont talk")
		
class Dog(Animal):
	def speak(self):
		print("woof")
		
class Cat(Animal):
	def speak(self):
		print("meow")
	
def makeDog(idCounter):
	'''
	@idCounter:int
	'''
	return Dog(idCounter)

def makeCat(idCounter):
	"""
	@idCounter:int
	"""
	return Cat(idCounter)

def main():
	ctr = 0
	aDog = makeDog(ctr)
	aDog.speak()
	
	aCat = makeCat(ctr)
	aCat.speak()

main()
a = 1