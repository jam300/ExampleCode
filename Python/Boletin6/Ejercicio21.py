"""21. Escriba una función que sume los n primeros números impares."""

def suma_impar(numero):
	suma=0
	Lista=[]
	for i in range(1,2*numero,2):
		suma+=i
		Lista.append(i)
	return (suma,Lista)




def main():
    numero=int(input("Dame un numero: "))
    resultado=suma_impar(numero)
    print("Los numeros impares a sumar son: ",resultado[1])
    print("La suma de esos numeros da: ",resultado[0])


if __name__ == '__main__':
    main()