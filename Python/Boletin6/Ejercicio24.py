"""24. DUF a la que se le pasa como parámetro una tabla que debe rellenar. Se leerá por teclado una
serie de números: guardaremos solo los pares e ignoraremos los impares. También hay que devolver la
cantidad de impares ignorados."""

def pares_impares():
	numero=1
	Tabla=[]
	contador=0

	while(numero>0):
		numero=int(input("Dame un numero: "))
		if(numero%2==0):
			Tabla.append(numero)
		elif(numero%2!=0 and numero>0):
			contador+=1

	print("La cantidad de numeros impares son: ",contador, " Los numeros guardados son: ", Tabla)




def main():
	print("Ingrese varios numero para cabar ingrese un numero negativo cualquiera")
	pares_impares()

	#print("La cantidad de numeros impares son: " " Los numeros guardados son: ", resultado[0])




if __name__ == '__main__':
    main()