"""7. utilizando dos tablas de tamaño 5x9 y 9x5, cargar la primera y trasponerla en la segunda."""

import random
def main():
	a, b = 5, 9  #a son las filas y b las columnas

	MatrixA = [[0 for x in range(b)] for y in range(a)]
	MatrixB = [[0 for x in range(a)] for y in range(b)]

	for i in range(a):
		for j in range(b):
			MatrixA[i][j]= random.randint(0,9)

	print("Matriz 5x9")

	for i in range(a):
		print(" ")
		for j in range(b):
			print(MatrixA[i][j],end=" ")

	for i in range(a):
		for j in range(b):
			MatrixB[j][i]= MatrixA[i][j]

	print(" ")
	print("-------------------------------")
	print("Matriz transpuesta de 9x5")

	for i in range(b):
		print(" ")
		for j in range(a):
			print(MatrixB[i][j],end=" ")

if __name__ == '__main__':
    main()