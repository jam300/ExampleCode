"""31. Calcular el factorial de n recursivamente."""



def factorial(numero):
	if(numero==0 or numero==1):
		return (1)
	elif(numero>1):
		return (numero*factorial(numero-1))

def main():
    numero=int(input("Dame un numero: "))
    print("El factorial de ",numero, " es: ", factorial(numero))

if __name__ == '__main__':
    main()