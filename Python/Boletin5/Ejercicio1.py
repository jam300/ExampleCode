"""1. Crear una tabla bidimensional de tamaño 5x5 y rellenarla de la siguiente forma: la posición T[n,m]
debe contener n+m. Después se debe mostrar su contenido."""

def main():

	# primero creamos la tabla de bidimensional de 5x5 llenas de ceros
	filas, columnas = 5, 5
	Matrix = [[0 for x in range(columnas)] for y in range(filas)]

	print(Matrix)
	for i in range(filas):
		for j in range(columnas):
			Matrix[i][j] = i+j
			
	for i in range(filas):
		print(" ")
		for j in range(columnas):
			print(Matrix[i][j], end=" ")

if __name__ == '__main__':
    main()