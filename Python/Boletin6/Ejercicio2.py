"""Este ejercicio engloba los ejercicio del 2-4. Hacer una funcion que devuelva el numero mayor y el menor de varios numeros"""

def minmax(Lista):
	max=0
	min=Lista[0]
	for i in range(len(Lista)):
		if (Lista[i]>max):
			max=Lista[i]
		if (Lista[i]<min):
			min=Lista[i]
	return[min,max]
#Otra forma de hacerlo usando la funcion sort()
def minmax2(Lista):
	Lista.sort()
	return[Lista[0],Lista[-1]]

#otra opcion seria usar la funcio minimo y maximo que tienen las listas
def minmax3(Lista):
	return[min(Lista), max(Lista)]

def main():
	lis=input("Introduzca los numeros separador por una coma: ")
	Lista=list(map(int, lis.split(",")))
	minimo, maximo= minmax(Lista)
	print("El maximo es: ", maximo, " y el minimo es: ", minimo," usando minmax")
	minimo, maximo= minmax2(Lista)
	print("El maximo es: ", maximo, " y el minimo es: ", minimo," usando minmax2")
	minimo, maximo= minmax3(Lista)
	print("El maximo es: ", maximo, " y el minimo es: ", minimo," usando minmax3")

if __name__ == '__main__':
    main()