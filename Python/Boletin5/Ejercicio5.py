"""5. Crear una tabla de tamaño 7x7 y rellenarla de forma que los elementos de la diagonal principal sean
1 y el resto 0."""


def main():
	filas    = int(input("Dame el numero de filas: "))
	columnas = int(input("Dame el numero de columnas: "))

	Matrix = [[0 for i in range(columnas)] for j in range(filas)]


	for i in range(filas):
		for j in range(columnas):
			if(i==j):
				Matrix[i][j]=1
			else:
				Matrix[i][j]=0


	for i in range(filas):
		print(" ")
		for j in range(columnas):
			print(Matrix[i][j],end=" ")


if __name__ == '__main__':
    main()