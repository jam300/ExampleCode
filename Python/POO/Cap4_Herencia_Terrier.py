from Cap4_Herencia_Dog import*

class TerrierDog(Dog):
	_breed = "Terrier dog"
	_bree_family = "Terrier"

	def __init__(self,name,age,favorite_toy,is_pregnant =False):
		super().__init__(name,age,favorite_toy,is_pregnant)
		print("TerrierDog created")

