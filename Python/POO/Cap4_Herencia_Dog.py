from Cap4_Herencia_domestico import*

class Dog(DomesticMammal):
	_number_of_legs = 4
	_breed = "Just a Dog"
	_breed_family = "Dog"

	def __init__(self, name, age, favorite_toy, is_pregnant=False):
		super().__init__(name,age,favorite_toy,is_pregnant)
		print("Dog created")

	def bark(self, times=1, other_domestic_mammal = None, is_angry = False ):
		message = self.name
		if other_domestic_mammal is not None:
			message += " to " + other_domestic_mammal.name + " : "
		else:
			message += " : "
		if is_angry:
			message += "Grr "
		message += "Woof " * times
		print(message)

	def talk(self):
		self.bark()

	@classmethod
	def print_breed(cls):
		print(cls._breed)

	@classmethod
	def print_breed_family(cls):
		print(cls._breed_family)




