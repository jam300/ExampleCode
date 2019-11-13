"""8. Crear una matriz “marco” de tamaño 8x6: todos sus elementos deben ser 0 salvo los de los bordes que
deben ser 1. Mostrarla."""

def main():
	filas, columnas = 8, 6
	Matrix = [[0 for x in range(columnas)] for y in range(filas)]

	for i in range(filas):
		for j in range(columnas):
			if(i==0 or i ==7):
				Matrix[i][j]=1
			if(j==0 or j==5):
				Matrix[i][j] = 1

	for i in range(filas):
		print(" ")
		for j in range(columnas):
			print(Matrix[i][j],end=" ")





if __name__ == '__main__':
    main()