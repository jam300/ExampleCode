import string


def main():
	list_letra = list(string.ascii_uppercase[:])  # lista de letras
	let = input("Introduzca una letra: ")  # pedir la letra
	index_letra = list_letra.index(let.upper())  # obtener le indice de la letra
	n = index_letra + 1

	for i in range(0, n):
		for k in range(n - 1, 0, -1):
			if k == i:
				print(list_letra[i], end="")
			else:
				print('*', end="")
		for j in range(0, n):
			if j == i:
				print(list_letra[i], end="")
			else:
				print('*', end="")

		print('')

	for i in range(n - 1, 0, -1):
		for k in range(n - 1, 0, -1):
			if k == i - 1:
				print(list_letra[i - 1], end="")
			else:
				print('*', end="")
		for j in range(1, n + 1):
			if (j == i):
				print(list_letra[i - 1], end="")
			else:
				print('*', end="")
		print('')


if __name__ == '__main__':
    main()