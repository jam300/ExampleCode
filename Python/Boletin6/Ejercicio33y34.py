"""33. DUF que calcule el n-ésimo término de la serie de Fibonacci. En esta serie el n-ésimo valor se
calcula sumando los dos valores anteriores. Es decir fibonacci(n) = fibonacci(n-
1)+fibonacci(n-2), siendo fibonacci(0)=1 y fibonacci(1)=1."""

def fibonacci(n):
	if(n==0):
		resultado=0
	elif (n==1 or n==2):
		resultado=1
	elif(n>2):
		resultado=fibonacci(n-1)+fibonacci(n-2)

	return (resultado)







def main():
    numero=int(input("Vamos calcular fibonacci(n).\nIntroduzca n (se recomienda n<40): "))
    hola=fibonacci(numero)

    print("El numero es: ",hola)



if __name__ == '__main__':
    main()