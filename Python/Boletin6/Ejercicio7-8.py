""" 7. Realizar una función que calcule (muestre en pantalla) el área o el volumen de un cilindro, según
se especifique. Para distinguir un caso de otro se le pasará el carácter 'a' (para área) o 'v'
(para el volumen). Además hemos de pasarle a la función el radio y la altura.
8. Ídem que devuelva una tabla con el área y el volumen."""

import math


def area_volumne(radio,altura):
	calculo = [math.pi*(radio*2)*altura, 2*math.pi*radio*altura + 2*math.pi*(radio*2)]
	return (calculo)


def main():
	radio=float(input("Dame el radio dle cilindro: "))
	altura=float(input("Dame la altura del cilindro: "))
	resultado=area_volumne(radio,altura)
	print("El area del cilindro es: %.2f y su volumen es: %.2f " % (resultado[1],resultado[0]))

if __name__ == '__main__':
    main()

