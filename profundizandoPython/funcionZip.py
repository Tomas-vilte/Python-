#print(dir(__builtins__))
#help(zip)

numeros = [1,2,3,4]
letras = ['a','b','c']
conjunto = {2,4,5,6,7,8,9}
identificadores = 324, 322, 323, 325, 324
mezcla = zip(numeros, letras, identificadores, conjunto)

#print(mezcla)
print(list(mezcla))
#print(tuple(zip(numeros, letras, identificadores, conjunto)))

# iterar en paralelo

for numero, letra, identificador, set in zip(numeros, letras, identificadores, conjunto):
    print('Numero:', numero, 'Letra:', letra, 'Identificador:', identificador, 'Aleatorio:', set)

nuevaLista = []
for numero, letra, identificador, set in zip(numeros, letras, identificadores, conjunto):
    nuevaLista.append(f'{identificador}-{numero}-{letra}-{set}')
    print(nuevaLista)

# unzip
mezcla = [(1,'a'),(2,'b'),(3,'c')]
numeros, letras = zip(*mezcla)
print('Numeros:', numeros, 'Letras:', letras)

# Ordenamiento usando zip

letras = ['b', 'a', 'c','e','d']
numeros = [5,3,2,4,1]
mezcla = zip(letras, numeros)
# Sin orden
print(f'Sin ordenar: {tuple(mezcla)}')

# Ordenar por letra (primer iterable)
print(f'Ordenados', sorted(zip(letras, numeros)))

# Crear un diccionario con zip y dos iterables

llaves = ['Nombre', 'Apellido', 'Edad']
valores = ['Juan', 'Perez', 18]
diccionario = dict(zip(llaves, valores))
print(diccionario)

# Actualizar elemento de un diccionario
llave = ['Edad']
nuevaEdad = [28]
diccionario.update(zip(llave, nuevaEdad))
print(diccionario)