#Creamos la clase padre o la mas basica la clase Animal
class Animal:
	_number_of_legs = 0 # variable numero de piernas protejido inicializado en0
	_Pairs_ayes = 0 # variable par de ojos protejido inicializado en 0

	def __init__(self,age):    #contructuro se inicializa poniendo la edad del animal
		self._age=age
		print("Animal created")  # imprime indicando que un animal fue creado


	@property
	def age(self):
		return self._age

	@age.setter
	def age(self,age):
		self._age = age


	def print_legs_and_ayes(self):
		print("I have " + str(self._number_of_legs) + " legs and " + str(self._pair_of_ayes *2 ) + " eyes. ")

	def print_ages(self):
		print("I am " + str(self._age) + " years old. ")

	def __lt__(self, other):
		return self.age < other.age

	def __le__(self, other):
		return self.age <= other.age

	def __gt__(self, other):
		return self.age > other.age

	def __ge__(self, other):
		return self.age >= other.age




