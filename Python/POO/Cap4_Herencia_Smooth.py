from Cap4_Herencia_Terrier  import*

class SmoothFoxTerrier(TerrierDog):
	_breed = "Smooth Fox Terrier"

	def __init__(self,name, age, favorite_toy, is_pregnant =False):
		super().__init__(name,age,favorite_toy,is_pregnant)
		print("SmoothFoxTerrier created")