"""30. DUF recursiva que calcule an."""


def potencia(base,exponente):

	if(exponente==0):
		resultado=1
	else:  #a a la n es igual a: a*an-1
		resultado = base*potencia(base,exponente-1)

	return (resultado)




def main():
    base=int(input("Dame un numero: "))
    exponente=int(input("Dame su exponente: "))
    print("el numero ",base, " elevado a la ", exponente, " es: ", potencia(base,exponente))


if __name__ == '__main__':
    main()