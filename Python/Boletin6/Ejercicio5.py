"""5. Función a la que se le pasan dos enteros y muestra todos los números comprendidos entre ellos,
inclusive."""


def mostrar(num1,num2):
	if(num1<num2):
		num1+=1
		for i in range(num1,num2,1):
			print(i,end=" ")
	else:
		for i in range(num2,num1,1):
			print(i,end=" ")
#Otra forma de hacer es usando la funcion minmax hecha anteriormente

def minmax3(Lista):
	return[min(Lista), max(Lista)]

def mostrar2(num1,num2):
	a,b=minmax3([num1,num2])
	for i in range(a+1,b,1):
		print(i,end=" ")

# una version donde combinas las dos funciona anteriores seria:

def mostrar3(num1,num2):
	a=[num1,num2]   # se guardan los numeros en una lista
	for i in range(min(a)+1,max(a),1):
		print(i, end=" ")
	#En el for se usa la funcion min  y max de las listas, el mas uno es para que range no contemple ese valor



def main():
	num1= int(input("Introduzca el numero 1: "))
	num2=int(input("Dame el numero 2: "))
	mostrar(num1,num2)
	print(" ")
	mostrar2(num1, num2)
	print(" ")
	mostrar3(num1, num2)



if __name__ == '__main__':
    main()