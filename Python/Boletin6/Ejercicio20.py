"""20.DUF que muestre en binario un número entre 0 y 255."""

def Binario(numero):
	resultado=[]
	contador=0
	binario=''
	if(int(numero)==0):
		resultado.append(0)
	else:
		while(int(numero)!=0):
			resultado.insert(contador,int(numero)%2)
			numero/=2
			contador+=1

	resultado.reverse()
	for i in resultado:
		binario+=str(i)
	return(binario)

# otra mejor opcion
def conversion(numero,base): # funcion de convercion cuyos datos de entrada son el numero a convertir y la base a usar
	resultado=[]    # lista para guardar el resultado de la operacion numero%base
	contador=0      # contador para el while que sirve para guardar la posicion en la lista resultado
	respuesta=''    # se guarda la respuesta final en una cadena de texto para que salga toda junta y no como una lista
	hexa={10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}  # para la base hexadecimal

	if(numero==0):
		resultado.append(0)         # si el numero es cero es cero para evitar divicion entre cero y dar error
	else:
		while(int(numero)!=0):      #mientras el nuemero entero sea mayor q ue cero se correo, ignoramos las fracciones
			resultado.insert(contador, int(numero%base))    # se gurda el resultado en la lista
			numero/=base    # se divide el numero entre la base para el siguiente vuelta del while
			contador+=1     # se incrementa el contador

	resultado.reverse() # la lista esta al revez hay que voltearla
	print(resultado)
	for i in resultado:
		if(10<=i<=15):      # si la bace es hexa para los numeros del 10-15 se cambia las letras
			respuesta+=str(hexa.get(i))
		else:
			respuesta+=str(i)   # de lo contrario cada numero se vuelve un str y se suma a la cadema respuesta

	return(respuesta)       # retorna el valor ya convertido

def main():
	base2={2:"Binario",8:"Octal",10:"Decimal",16:"Hexadecimal"}  # para el mensaje de salida
	numero=int(input("Introduzca un numero entero positivo: "))
	base=int(input("Dame la base: "))
	print("El numero ",numero," en base ", base2.get(base)," es ",conversion(numero,base))
	print(bin(numero))
	print(hex(numero))
	print(oct(numero))



if __name__ == '__main__':
    main()
