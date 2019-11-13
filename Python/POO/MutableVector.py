class MutableVector3D:
	def __init__(self,x,y,z):
		self.__x = x
		self.__y = y
		self.__z = z

	def sum(self,deltax,deltay,deltaz):
		self.__x += deltax
		self.__y += deltay
		self.__z += deltaz

	@property
	def x(self):
		return self.__x

	@x.setter
	def x(self,x):
		self.__x=x

	@property
	def y(self):
		return self.__y

	@y.setter
	def y(self, y):
		self.__y = y

	@property
	def z(self):
		return self.__z

	@z.setter
	def z(self, z):
		self.__z = z

	@classmethod
	def origin_vector(cls):
		return cls (0,0,0)

class InmutableVector3D:

	def __init__(self,x,y,z):
		self.__x = x
		self.__y = y
		self.__z = z

	def sum(self, deltax,deltay,deltaz):
		return type(self)(self.__x + deltax, self.__y + deltay, self.__z +deltaz)

	@property
	def x(self):
		return self.__x

	@property
	def y(self):
		return self.__y


	@property
	def z(self):
		return self.__z

	@classmethod
	def equal_elements(cls,initial_value):
		return  cls(initial_value,initial_value,initial_value)

	@classmethod
	def origin_vector(cls):
		return cls.equal_elements(0)


mutable = MutableVector3D.origin_vector()
mutable.sum(5,10,15)
print(mutable.x, mutable.y, mutable.z)

inmutable = InmutableVector3D.origin_vector()
print(inmutable.x,inmutable.y,inmutable.z)
inmutable.sum(1,2,3)
print(inmutable.x,inmutable.y,inmutable.z)
inmutable2 = inmutable.sum(1,2,3)
print(inmutable2.x,inmutable2.y,inmutable2.z)

