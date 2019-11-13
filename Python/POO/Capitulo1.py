import math

class TibetanSpaniel:
	family= "Companion, herding"
	area_of_origin = "Tibet"
	learning_rate = 9
	obedience = 3
	problem_solving =8

	def __init__(self, name, favorite_toy, watchdog_habiity):
		self.__name = name
		self.__favorite_toy = favorite_toy
		self.__watchdog_hability = watchdog_habiity

	@property
	def name(self):
		return self.__name

	@property
	def favorite_toy(self):
		return self.__favorite_toy

	@favorite_toy.setter
	def favorite_toy(self,favorite_toy):
		self.__favorite_toy=favorite_toy

	@property
	def watchdog_hability(self):
		return self.__watchdog_hability

	@watchdog_hability.setter
	def watchdog_hability(self,watchdog_hability):
		if watchdog_hability<0:
			self.__watchdog_hability = 0
		elif watchdog_hability>10:
			self.__watchdog_hability = 10
		else:
			self.__watchdog_hability = watchdog_hability

	@property
	def protection_score(self):
		return math.floor ( ( self.__watchdog_hability + type(self).learning_rate + type(self).problem_solving)/3 )





brain = TibetanSpaniel("Brain","Talking Minion",4)
#print(brain.name)
#print(brain.favorite_toy)
#brain.favorite_toy="boune"
#print(brain.favorite_toy)
hugo = TibetanSpaniel("hugo","pop",7)
print(hugo.watchdog_hability)
hugo.watchdog_hability = -5
print(hugo.watchdog_hability)
hugo.watchdog_hability = 30
print(hugo.watchdog_hability)
hugo.watchdog_hability = 8
print(hugo.watchdog_hability)
print(hugo.protection_score)