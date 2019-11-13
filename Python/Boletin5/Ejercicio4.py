"""4. Crear y cargar una tabla de tamaño 3x3, trasponerla y mostrarla. Solo funciona para matrices de 3x3"""

def main():

	filas    = int(input("Dame el numero de filas: "))
	columnas = int(input("Dame el numero de columnas: "))

	Matrix=[]
	for i in range(filas):
		Matrix.append([0]*columnas)

	for i in range(filas):
		for j in range(columnas):
			Matrix[i][j]=int(input('Dame el componente (%d,%d): ' % (i,j)))

	for i in range(filas):
		print(" ")
		for j in range(columnas):
			print(Matrix[i][j],end=" ")


	for i in range(filas):
		for j in range(0,i,1):
			aux=Matrix[i][j]
			Matrix[i][j]=Matrix[j][i]
			Matrix[j][i]=aux
	print(" ")
	print("-----------------------------")
	print("Matriz transpuesta")

	for i in range(filas):
		print(" ")
		for j in range(columnas):
			print(Matrix[i][j],end=" ")






if __name__ == '__main__':
    main()