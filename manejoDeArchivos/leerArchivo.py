try:
    archivo = open('c:\\users\michu\desktop\python\prueba.txt', 'r')
    #print(archivo.read())
except FileNotFoundError:
    pass
finally:
    pass

# leer algunos caracteres
#print(archivo.read(3))
#print(archivo.read(5))

# leer lineas completas
#print(archivo.readline())
#print(archivo.readline())

# Iterar el archivo
#for linea in archivo:
#    print(linea)

# Leer lineas
#print(archivo.readlines())

# Acceder a una linea de la lista
#print(archivo.readlines()[1])

#abrimos un nuevo archivo
# a - anexar informacion
archivo2 = open('copia.txt', 'a')
archivo2.write(archivo.read())

archivo.close()
archivo2.close()

print('Se ha terminado el proceso de leer y copiar archivos')