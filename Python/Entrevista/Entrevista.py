def main():
    numero = int(input("Introduzca un numero: "))
    print(convergence(numero))

def NumDigitos(numero):
    if numero>9:
        numero = int(numero/ 10)
        return 1 + NumDigitos(numero)
    elif numero<=9:
        return 1

def convergence(numero):
    digitos=NumDigitos(numero)
    total=1
    if digitos == 1:
        return 0
    else:
        for i in range(1, digitos + 1):
            NewNumber = int(numero / 10 ** (digitos - i))
            numero = int(numero % 10 ** (digitos - i))
            total *= NewNumber
        return 1 + convergence(total)

if __name__ == '__main__':
    main()