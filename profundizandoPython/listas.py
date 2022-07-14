# Profundizando listas
# Lista son mutables

nombres = ['Juan', 'Karla', 'Pedro']
nombres1 = 'Laura Maria Gonzalo Ernesto'.split()
# Sumar listas
print(f'Sumar listas: {nombres + nombres1}')
# Extender una lista con otra lista
nombres.extend(nombres1)
print(f'Extender la lista1 con las lista2:: {nombres}')

# Lista de numeros
numeros = [10, 40, 15, 4, 20, 90, 4]
print(f'Lista original: {numeros}')
# Obtener el indice del primer elementos encontrado en una lista
#help(list.index)
print(f'Indice 4: {numeros.index(4)}')

# Invertir el orden de los elementos de una lista
numeros.reverse()
print(f'Lista invertida: {numeros}')

# Ordenar los elementos de una lista
numeros.sort()
print(f'Lista ordenada (ascendente): {numeros}')

# Ordenar de manera descendente una lista
numeros.sort(reverse=True)
print(f'Lista ordenada (descendente): {numeros}')

# Obtener valor min y max de una lista

print(f'Valor minimo: {min(numeros)}')
print(f'Valor maximo {max(numeros)}')

# Copiar de una lista

numeros2 = numeros.copy()
#help(list.copy)
print(f'Lista copiada: {numeros2}')
print(f'Misma referencia: {numeros is numeros2}')
print(f'Mismo contenido: {numeros == numeros2}')

# Podemos usar el constructor de la lista

numeros2 = list(numeros)
print(f'Misma referencia: {numeros is numeros2}')
print(f'Mismo contenido: {numeros == numeros2}')

# slicing

numeros2 = numeros[:]
print(f'Misma referencia: {numeros is numeros2}')
print(f'Mismo contenido: {numeros == numeros2}')

# Multiplicacion listas

listaMultiplicacion = 5*[[2, 5]]
print(listaMultiplicacion)
print(f'Misma referencia: {listaMultiplicacion[0] is listaMultiplicacion[1]}')
print(f'Mismo contenido: {listaMultiplicacion[0] == listaMultiplicacion[1]}')
listaMultiplicacion[2].append(10)
print(listaMultiplicacion)

# Matrices en python

matriz = [[10, 20], [30, 40, 50], [60, 70, 80, 90]]
print(f'Matriz original: {matriz}')
print(f'Renglon 0, Columna 0: {matriz[0][0]}')
print(f'Renglon 2, Columna 3: {matriz[2][3]}')
matriz[2][0] = 65
print(f'Matriz modificada: {matriz}')

listaListas = [[10, 14, 87, 90 ,71],[4, 5, 6, 7],[9, 0, 11, 15, 45, 61, 70]]
listaListas.sort(key=len)
print(f'Ordenar lista: {listaListas}')

# sorted built - in

# help(sorted)

nombres3 = ['Juan Carlos', 'Karla', 'Pedro', 'Esperanza']
nombres3 = sorted(nombres3)
print(nombres3)

# Ordenar de manera descendente
nombres3 = sorted(nombres3, reverse=True)
print(nombres3)

# Ordenar por la cantidad de caracteres (Largo)
nombres3 = sorted(nombres3, key=len)
print(nombres3)

# built - in reversed
nombres3 = reversed(nombres3)
print(list(nombres3))