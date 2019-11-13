n=3
for i in range(n+1):
	for j in range(n-i):
		print('*', end="")
	for k in range(2*i-1):
		print('*',end="")
	print("")

for i in range(n-1,0,-1):
	for j in range(n-i):
		print('*', end="")
	for k in range(2*i-1):
		print('*',end="")
	print("")

n=5
#cuadrante ++
for i in range(0,2*n-1):
    for j in range(0,2*n-1):
        print('*',end="")
    print(" ")