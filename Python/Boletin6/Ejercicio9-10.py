"""9. Módulo al que se le pasa un número entero y devuelve el número de divisores primos que tiene."""
"""10.Ídem diseñar una función que devuelve una tabla con los divisores."""

import math

def es_primo(numero):
	primo =True
	i=2

	if((numero%math.sqrt(numero))==0 and numero%2==0):
		primo=False

	while(i<numero and primo==True):
		if (numero%i==0):
			primo=False
		i+=1
	return (primo)

def num_divisores(numero):
	contador=1

	for i in range(2,numero+1,1):
		if(es_primo(i) and numero%i==0):
			contador+=1

	return (contador)

def divisores(numero):
	contador=0
	divisor=[]
	#divisor=[None]*num_divisores(numero)

	for i in range(1,numero+1,1):
		if(es_primo(i) and numero%i==0):
			divisor.append(i)
			contador+=1
	print(divisor)

	return(divisor)

def main():
    numero=int(input("Dame un numero: "))
    divisor=divisores(numero)
    print("Los divisores de ", numero, " son: ")

    for i in range(len(divisor)):
	    print(divisor[i],end=" ")


if __name__ == '__main__':
    main()