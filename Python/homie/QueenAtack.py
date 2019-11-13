def attack(farg):
	if ((farg[0]==farg[2]) or farg[1]==farg[3]):
		print("Las damas se estan atacando ")
	elif(abs(farg[0]-farg[2]) == abs(farg[1]-farg[3])):
		print("Las damas se estan atacando por la diagonal")
	else:
		print("Las damas no se estan atacando")

def tablero(farg):
	for i in range(0,9):
		for j in range(0,9):
			if(i==farg[0] and j==farg[1]):
				print('W',end="")
			elif (i == farg[2] and j == farg[3]):
				print('B', end="")
			else:
				print('-', end="")
		print('')

def main():
	print("Introduzca las coordenadas de las damas de la sigueinte manera: /n")
	print("blanca_filas,blanca_columna,negra_fila,negra_columna del 1-9",end="")
	lista=input(" : ")
	coordenadas=list(map(int, lista.split(",")))
	attack(coordenadas)
	tablero(coordenadas)



if __name__ == '__main__':
    main()