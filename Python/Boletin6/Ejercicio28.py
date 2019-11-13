"""28. DUF que ordene la tabla que se le pasa."""

import random

#ordenacion por intercambio
def ordenar_tabla(Tabla):
	#aux=0
	for i in range(0,len(Tabla),1):
		for j in range(0,len(Tabla)-1,1):
			if(Tabla[j]>Tabla[j+1]):
				aux=Tabla[j]
				Tabla[j]=Tabla[j+1]
				Tabla[j+1]=aux

	return (Tabla)





def tabla_randon(cantidad):
	Lista=[]

	for i in range(0,cantidad,1):
		Lista.append(random.randint(0,cantidad))
	return(Lista)


def main():
	cantidad=int(input("Cuantos numeros quieres?: "))
	Tabla=tabla_randon(cantidad)
	print("La tabla desordenada es: ")
	print(Tabla)
	print("---------------------------------")
	print("La tabla ordenada es: ")
	print(ordenar_tabla(Tabla))




if __name__ == '__main__':
    main()