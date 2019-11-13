"""3. Crear y cargar dos matrices de tamaño 3x3, sumarlas y mostrar su suma."""

def main():
	filas, columnas = 3, 3
	MatrixA = [[0 for x in range(columnas)] for y in range(filas)]
	MatrixB = [[0 for x in range(columnas)] for y in range(filas)]
	Suma = [[0 for x in range(columnas)] for y in range(filas)]

	for i in range(filas):
		for j in range(columnas):
			MatrixA[i][j] = int(input('Dame el componente (%d,%d) de la Matriz A:' % (i, j)))

	for i in range(filas):
		for j in range(columnas):
			MatrixB[i][j] = int(input('Dame el componente (%d,%d) de la matriz B: ' %(i,j)))


	for i in range(filas):
		for j in range(columnas):
			Suma[i][j]=MatrixA[i][j] + MatrixB[i][j]


	for i in range(filas):
		print(" ")
		for j in range(columnas):
			print(Suma[i][j],end=" ")



if __name__ == '__main__':
    main()