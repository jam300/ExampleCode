def prin_song (*args):
	print("{0} bottles of beer on the wall, {1} bottles of beer\n \
		{2},{3} bottles of beer on the wall.".format (args[0],args[0],args[1],args[2]))

def song(bottles):
	frase = ['Take one down and pass it around','No more','Go to the store and buy some more']
	if bottles>=2:
		prin_song(bottles,frase[0],(bottles-1))
	elif bottles == 1:
		prin_song(bottles,frase[0],frase[1])
	elif bottles ==0:
		prin_song(frase[1],frase[2],99)	

def main():
	 [song(bottles) for bottles in range(99, -1, -1)]	 	

if __name__ == '__main__':
	main()