"""Esta ejercicio abarca los ejercicio del 11-16 del boletin 6 del libro
"Ejercicios de programacion en java (ADA)"
 crea un programa que calcule el Maximo comun divisor, mcd y el Minimo comun multiplo de varios numeros"""

#funcion Maximo Comun Divisor
def mcd(Lista):
	Lista.sort()     #Ordeno la Lista de menor a mayor
	MCD=0
	for i in range(1,Lista[0]+1,1):  # rango llega hasta el numero mas chico, ya que este pone el limite
		divide = True    # se inicializa una variable que con cada vuelta se vuelve True
		for j in Lista:
			if(j%i!=0):   # si el modulo de j con i da diferente de cero, i no puede ser un MCD
				divide=False # para todos los elementos que contenga la Lista
		if(divide):
			MCD=i       # si la bandera divide es true quiere decir que que  i divide a todos por igual
						# e i  es el Maxicmo comun divisor MCD, MCD se actualiza con cada iteracion

	return(MCD)         # se retorna el valor de MCD

# funcion para el minimo comun multiploo MCM
def mcm(Lista):
	Lista.sort()    # orden lista de menor a mayor
	residuo=[]
	MCM=mcd(Lista)  # se conboca la funcion MCD maximo comun divisor el resultado se guarda en MCM
	mul=1           # se inizaliza mul =1
	contador=0      # se inicializa contador =1
	for i in Lista:     # para cada elemento  en Lista
		residuo.append(int(i/MCM))   # se divide por el MCD y se guarda en la lista residuo
	for i in range(len(residuo)):
	#while(contador<len(residuo)):   # se corre el while tantas veces haya elementos en residuo
		# se usa la formula: MCM = a*b/MCD(a,b)
		# donde a es el elemento mul resultado de la operacion en la ultima interacion
		# y b el elemento siguiente de la lista residuo
		mul=(int(mul)*int(residuo[i]))/mcd([int(mul),int(residuo[i])])
		#contador+=1 # se incrementa el contador

	return(int(mul*MCM))


def main():
	lista=input("Dame los numeros a analizar separados por comas: ") # se pide los numeros a analizar
	Lista=list(map(int, lista.split(",")))  #
	print("El maximo comun divisor es: ", mcd(Lista))
	print("El minimo comun multiplo es: ", mcm(Lista))  #se imprimen



if __name__ == '__main__':
    main()