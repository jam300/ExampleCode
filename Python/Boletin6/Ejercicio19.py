"""19.Diseña una función (en adelante DUF) que calcule A a la n ."""



def exponen(numero, expo):
	res=0
	if(expo==0):
		res=1
	else:
		res=numero**expo
	return(res)

def main():
	numero=int(input("Dame la base: "))
	expo=int(input("Dame su su exponente: "))
	resutado= exponen(numero, expo)
	print('El numero %d elevado a la %d es %d' %(numero,expo,resutado))

if __name__ == '__main__':
    main()