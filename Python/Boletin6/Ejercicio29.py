"""29. DUF que toma como parámetros dos tablas. La primera con los 6 números de una apuesta de la
primitiva, y la segunda con los 6 números ganadores. La función debe devolver el número de
aciertos."""

import random

def resultados(apuesta,combinacion):
	contador=0
	for i in range(6):
		if(apuesta[i]==combinacion[i]):
			contador+=1

	return (contador)




def loteria():
	tabla = []
	for i in range(6):
		a = random.randint(1, 49)
		if (a in tabla):
			a = random.randint(1, 49)
		else:
			tabla.append(a)
	return (tabla)


def main():
	apuesta=[]
	contador=0
	print("Introduzca los 6 numeros para su apuesta del 1 al 49 no repetidos")
	print(" ")
	while(contador<6):
		a=int(input("Dame el numero " + str(contador+1) + " : "))
		if(1<=a<=49):
			apuesta.append(a)
			contador+=1
		else:
			print("Numero fuera del rango, tiene que ser entre 1 y 49")


	combinacion=loteria()
	print("la apuesta quedo asi: Numero ganadores         Tu apuesta")
	for i in range(6):
		print(combinacion[i],"      ",apuesta[i])

	b=resultados(apuesta,combinacion)

	if(b==0):
		print("Mejor suerte la proxima vez ")
	else:
		print("ha tenido ",b," aciertos")


if __name__ == '__main__':
    main()


