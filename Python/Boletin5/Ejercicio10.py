"""11-Se pretende realizar un programa para gestionar la lista de participaciones en una competición de
salto de longitud. El número de plazas disponible es de 10. Sus datos se irán introduciendo en el
mismo orden que vayan inscribiéndose los atletas. Diseñar el programa que muestre las siguientes
opciones:
                        1- Inscribir un participante.
                        2- Mostrar listado de datos.
                        3- Mostrar listado por marcas.
                        4- Finalizar el programa.

Si se selecciona 1, se introducirán los datos de uno de los participantes: Nombre, mejor marca del
2002, mejor marca del 2001 y mejor marca del 2000.
Si se elige la opción 2, se debe mostrar un listado por número de dorsal.
La opción 3 mostrará un listado ordenado por la marca del 2002, de mayor a menor.
Tras procesar cada opción, se debe mostrar de nuevo el menú inicial, hasta que se seleccione la
opción 4, que terminará el programa."""



def Inscripcion(Matrix):
	#comprobar = 0

	for i in range(3):
		#puesto = True
		if (Matrix[i][0] == 0):
			Matrix[i][0] = input("Dame el nombre del participate: ")
			#while (puesto == True):
			#	dorsal = int(input("Introduzca el numero de dorsal: "))
			#	if (dorsal == comprobar):
			#		print("numero ocupado introduzca otro numero")
			#	else:
			#		Matrix[i][1] = dorsal
			#		puesto = False
			#comprobar = Matrix[i][1]
			Matrix[i][1] = i+1
			Matrix[i][2] = int(input("Dime  su marca del 2000: "))
			Matrix[i][3] = int(input("Dime  su marca del 2001: "))
			Matrix[i][4] = int(input("Dime  su marca del 2002: "))
		else:
			print("Ya no hay lugar para otro participante")
	return(Matrix)

def Listad_Datos(Matrix):
	Matrix.sort(key=lambda x: x[1], reverse=True)
	for i in range(10):
		print(" ")
		for j in range(5):
			if (Matrix[i][j] != 0):
				print(Matrix[i][j], end=" ")
	print(" ")

def marca(Matrix):
    Matrix.sort(key=lambda x : x[4], reverse=True)
    for i in range(10):
        print(" ")
        for j in range(5):
            if (Matrix[i][j] != 0):
                print(Matrix[i][j], end=" ")
    print(" ")



def main():
    filas, columnas = 10, 5
    Matrix = [[0 for x in range(columnas)] for y in range(filas)] # se inicializa la matriz de 10x5
    valor=True

    """Ejemplo de como quedara la matriz
        [Nombre_participate,#dorsal,Marca_2000,Marca_2001,Marca_2002]           
    """


    while(valor):
        print("Escoge una opcion: ")
        print(" 1 = Inscribir un participante.")
        print(" 2 = Mostrar listado de datos.")
        print(" 3 = Mostrar listado por marcas.")
        print(" 4 = Finalizar el programa. ")
        print(" ")
        entrada= int(input())
        if(entrada<=0 or entrada>= 5):
            print("Opcion no disponible")
        elif(entrada==1):
            print("Escogiste la opcion uno")
            Inscripcion(Matrix)
        elif(entrada==2):
            print("Escogiste la opcion dos")
            Listad_Datos(Matrix)
        elif(entrada==3):
            print("Escogiste la opcion tres")
            marca(Matrix)
        elif(entrada==4):
            valor = False















if __name__ == '__main__':
    main()


