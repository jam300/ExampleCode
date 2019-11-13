"""6. Crear y cargar una tabla de tamaño 10x10, mostrar la suma de cada fila y de cada columna."""

def main():
	filas = int(input("Dime el numero de filas: "))
	columnas = int(input("Dime el numero de columnas: "))

	Matrix = []


	for i in range(filas):
		Matrix.append( [0]*columnas)           # se crea la matriz de ceros
		for j in range(columnas):
			Matrix[i][j]=int(input('Dame el componente(%d,%d): ' % (i,j))) # se va insertando los valores

	for i in range(filas):
		suma_filas    = 0
		suma_columnas = 0
		for j in range(columnas):
			suma_filas    += Matrix[i][j]   # va sumando elemento por elemento de cada fila
			suma_columnas += Matrix[j][i]   # va sumando elemento por elemento de cada columna
		print("La suma de fila "    ,i, " es " ,suma_filas)
		print("La suma de columna " ,i, " es " ,suma_columnas)

	for i in range(filas):
		print(" ")
		for j in range(columnas):
			print(Matrix[i][j],end=" ")

	print(" ")




if __name__ == '__main__':
    main()
