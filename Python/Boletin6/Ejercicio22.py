"""22. Dado el valor de un ángulo, sería interesante saber su seno, coseno y tangente. Escribir una
función que muestre en pantalla los datos anteriores."""

import math
def info_angulo(angulo):
	angulo=math.pi/(180*angulo)
	print("Coseno: ",math.cos(angulo))
	print("Seno: ", math.sin(angulo))
	print("Tangente: ", math.tan(angulo))
	print(angulo)



def main():
	angulo=int(input("Dame el angulo de 0-360 grados: "))
	info_angulo(angulo)

if __name__ == '__main__':
    main()