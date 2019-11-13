"""
columnas, filas = 2,3
Matrix = [[0 for x in range(columnas)] for y in range(filas)]
print(Matrix)
Matrix[1][0]=1
print(Matrix)
Matrix[2][0]=48
print(Matrix)

for fila, columnas in Matrix:
	print(fila,columnas)

for i in range(3):
	print(" ")
	for j  in range(2):
		print(Matrix[i][j],end=" ")
"""

"""m=int(input("Dame el numero de filas: "))
n=int((input("Dame el numero de columnas: ")))
M=[]
for i in range(m):
	M.append([0] * n)

for i in range(m):
	for j in range(n):
		M[i][j]=int(input('Dame le componente (%d,%d):' %(i,j)))


for i in range(m):
	print(" ")
	for j  in range(n):
		print(M[i][j],end=" ")


print(" ")
print(" ")
filas, columnas = 10, 5
Matrix = [[0 for x in range(columnas)] for y in range(filas)] # se inicializa la matriz de 10x5
for i in range(10):
	print(" ")
	for j in range(5):
		print(Matrix[i][j],end=" ")

print(" ")
for i in range(2):
	Matrix[i][0] = input("Dame el nombre del participate: ")
	Matrix[i][1] = int(input("Introduzca el numero de dorsal: "))
	Matrix[i][2] = int(input("dime  su marca del 2000: "))
	Matrix[i][3] = int(input("dime  su marca del 2001: "))
	Matrix[i][4] = int(input("dime  su marca del 2002: "))

for i in range(10):
	print(" ")
	for j in range(5):
		if(Matrix[i][j]!=0):
			print(Matrix[i][1],end=" ")"""
"""from operator import itemgetter
inputlist = [
[1, 0.23],
[2, 0.39],
[4, 0.31],
[5, 0.27],
]
sorted(inputlist, key=itemgetter(1), reverse=True)
for i in range(4):
	print(" ")
	for j in range(2):
		print(inputlist[i][j], end=" ")"""

ulist = [[1, 0.23,9,3,5],[5, 0.39,5,5,8],[9, 0.31,6,9,6],[7, 0.27,1,6,3]]

b=ulist[1][2]
print(b)
for i in range(4):
	print(" ")
	for j in range(5):
		print(ulist[i][j],end=" ")

ulist.sort(key=lambda x : x[2], reverse=True)
print(" ")
for i in range(4):
	print(" ")
	for j in range(5):
		print(ulist[i][j],end=" ")
