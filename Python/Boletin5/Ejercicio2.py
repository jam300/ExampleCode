"""2. Crear y cargar una tabla de tamaño 4x4 y decir si es simétrica o no, es decir si se obtiene la
misma tabla al cambiar las filas por columnas."""

def main():
	filas, columnas = 4, 4
	Matrix = [[0 for x in range(columnas)] for y in range(filas)]  #se crea la matrix 4x4

	# Se introduce los valores de la amtrix por teclado

	for i in range(filas):
		for j in range(columnas):
			Matrix[i][j] = int(input('Dame le componente (%d,%d):' % (i, j)))

	simetrica=True
	i=0
	while(i<4 and simetrica==True):
		j=0
		while(j<i and simetrica==True):
			if(Matrix[i][j]!=Matrix[j][i]):
				simetrica=False
			j+=1
		i+=1

	if(simetrica):
		print("Si es metrica")
	else:
		print("No es simetrica")




if __name__ == '__main__':
    main()
