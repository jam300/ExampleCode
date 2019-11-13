from Cap4_Herencia import*

class Mammal(Animal):
	_Pairs_ayes = 1

	def __init__(self, age, is_pregnant = False):
		super().__init__(age)
		self._is_pregnant = is_pregnant
		print("Mammal Created")

	@property
	def is_pregnat(self):
		return self._is_pregnant

	@is_pregnat.setter
	def is_pregnant(self,is_pregnat):
		self._is_pregnant = is_pregnat









