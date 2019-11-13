"""6. Función que muestra en pantalla el doble del valor que se le pasa como parámetro."""

def doble(numero):
	print(numero*2)


def main():
	numero=float(input("Dame un numero: "))
	doble(numero)

if __name__ == '__main__':
    main()