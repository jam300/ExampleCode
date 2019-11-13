from Cap_4_Herencia_Mamifero import*

class DomesticMammal(Mammal):
	def __init__(self,name,age,favorite_toy,is_pregnant =False):
		super().__init__(age,is_pregnant)
		self._name = name
		self._favorite_toy = favorite_toy
		print("Domestic Mammal created")


	@property
	def name(self):
		return self._name

	@property
	def favorite_toy(self):
		return self._favorite_toy

	@favorite_toy.setter
	def favorite_toy(self,favorite_toy):
		self._favorite_toy = favorite_toy

	def talk(self):
		print(self._name + " : talks")







