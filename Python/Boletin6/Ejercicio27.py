"""27.Diseñar la función opera_tabla, a la que se le pasa dos tablas, el número de elementos útiles y
que operación se desea realizar: sumar, restar, multiplicar o dividir (mediante un carácter: 's',
'r', 'm', 'd'). La función debe devolver una tabla con los resultados."""


def opera_tabla(Tabla1,Tabla2,operacion,utiles):
	resultado=[]
	if (operacion=='S'):
		for i in range(0,utiles,1):
			resultado.append(Tabla1[i]+Tabla2[i])
	if(operacion=='R'):
		for i in range(0,utiles,1):
			resultado.append(Tabla1[i]-Tabla2[i])
	if (operacion =='D'):
		for i in range(0,utiles,1):
			resultado.append(Tabla1[i]/Tabla2[i])
	if(operacion=='M'):
		for i in range(0,utiles,1):
			resultado.append(Tabla1[i]*Tabla2[i])

	return(resultado)

def main():
    lista=input("Introdusca los numero de la tabla 1 separados por comas: ")
    Tabla1=list(map(int,lista.split(",")))
    lista = input("Introdusca los numero de la tabla 2 separados por comas: ")
    Tabla2 = list(map(int, lista.split(",")))
    operacion=input("Que operacion va realizar?, suma,resta, division, multipliacion (S,R,D,M): ")
    utiles=int(input("Diga el numero de elementos con los cuales quiere realizar la operacion: "))
    a=opera_tabla(Tabla1,Tabla2,operacion,utiles)
    print("El resultado de la operacion de las tablas es: ",a)




if __name__ == '__main__':
    main()