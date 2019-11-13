"""9. Hacer lo mismo que el ejercicio anterior, pero con una matriz 9x9x9. Creamos un cubo con las caras
puestas a 1 y el interior a 0."""


def main():
	filas, columnas,ancho = 3,3,3
	Matrix = [[[0 for x in range(columnas)] for y in range(filas)] for z in range(ancho)]


	for i in range(filas):
		for j in range(columnas):
			for k in range(ancho):
				if(i==0 or i ==2):
					Matrix[i][j][k]=1
				if(j==0 or j==2):
					Matrix[i][j][k] = 1
				if(k==0 or k==2):
					Matrix[i][j][k]=1





	for i in range(filas):
		print(" ")
		for j in range(columnas):
			print(" ")
			for k in range(ancho):
				print(Matrix[i][j],end=" ")


if __name__ == '__main__':
    main()