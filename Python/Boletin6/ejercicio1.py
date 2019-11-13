"""1. Realizar una función, a la que se le pase como parámetro un número N, y muestre por pantalla N
veces, el mensaje: “Módulo ejecutándose”"""

def mostrar(num):
    for i in range(num):
        print(i+1, "Modulo ejecuntandose")

def main():
    num=int(input(" Introduzca un numero: " ))
    print("-----------------------------------")
    mostrar(num)
    print("-----------------------------------")
	


if __name__ == '__main__':
    main()