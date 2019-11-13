""" 25. DUF a la que se le pasa una tabla de enteros y un número. Debemos buscar el número en la tabla e
indicar si se encuentra o no.
26. Igual que el ejercicio anterior, pero suponiendo que la tabla no está siempre llena, y el número
de elementos se pasa también como parámetro.
convinare estos dos ejercicio pasando por parametro el numero de elementos que tendra la lista
y se llenaran al hazar con numero enteros y se procedera a adivinar el numero"""

import  random
def adivina(dimension, numero):
	Lista=[]
	adivinar=False
	for i in range(dimension):
		Lista.append(random.randint(1,dimension))
	while(adivinar==False):
		if(numero in Lista):
			print("El numero se encuentro en la lista")
			adivinar=True
		else:
			print("El numero no esta en la lista")
			numero=int(input("Adivine de nuevo: "))


def main():
    dimension=int(input("Introduzca la dimension de la lista: "))
    numero=int(input("Dame un numero a buscar: "))
    #print(random.randint(1,10))
    adivina(dimension,numero)

if __name__ == '__main__':
    main()