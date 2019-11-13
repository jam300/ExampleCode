"""23. Diseñar una función que calcule la distancia euclídea de dos puntos."""

import math
def distancia_euclidiana(puntos):
	return(math.sqrt(math.pow((puntos[2]-puntos[0]),2) + math.pow((puntos[3]-puntos[1]),2)))



def main():
    lista=input("Dame las coordenadas del punto 1 de la sigueinte forma (x,y): ")
    puntos=list(map(int,lista.split(",")))
    lista = input("Dame las coordenadas del punto 2 de la sigueinte forma (x,y): ")
    puntos += list(map(int, lista.split(",")))
    print(puntos)
    print("La distancia euclidiana es %.2f" %distancia_euclidiana(puntos))

if __name__ == '__main__':
    main()
