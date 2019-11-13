from django.db import models

class Nodo(models.Model):
	Nombre = models.CharField(max_length=100)
	SerialNumber = models.CharField(max_length=100,default='SOME STRING') #unique=True agrega para que sea unico
	Descripcion = models.TextField()

	def __str__(self):
		return self.Nombre

class Variable(models.Model):
	nodo = models.ForeignKey(Nodo, on_delete=models.CASCADE)
	Data_time = models.DateTimeField()
	Voltaje = models.DecimalField(max_digits=7, decimal_places=3)
	Corriente = models.DecimalField(max_digits=10, decimal_places=3)
	Watts = models.DecimalField(max_digits=10, decimal_places=3)
	VA = models.DecimalField(max_digits=10, decimal_places=3)
	VAR = models.DecimalField(max_digits=10, decimal_places=3)
	FP = models.DecimalField(max_digits=3, decimal_places=2)

	def __dir__(self):
		return ["Voltaje", "Corriente", "Watts","VA","VAR","FP"]
