from io import open



ficheros=open('fichero.txt', 'r')
texto5=ficheros.readlines()
print(texto5)
ficheros.close()