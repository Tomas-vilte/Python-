numeros = range(10)
listaPares = []

# Creamos una nueva lista con los valores pares
for numero in numeros:
    # Revisamos si es un numero par
    if numero % 2 == 0:
        listaPares.append(numero*numero)

print(f'Lista pares: {listaPares}')

# Hacemos lo mismo pero con list comprehensions
# [expresion for var in coleccion if condicion]
# La condicion del if es opcional
listaPares = []
listaPares = [numero*numero for numero in numeros if numero % 2 == 0]
print(f'Lista pares con list comprehensions: {listaPares}')

# Un ejemplo similar con dos condiciones (las condiciones son opcionales)
# Solo se agrega el valor a la lista cuando el valor cumple con ambas condiciones
# Es decir, debe ser divisible entre 2 y divisible entre 6

pares = [numero for numero in range(50) if numero % 2 == 0 if numero % 6 == 0]
print(f'Lista divisible por 2 y 6: {pares}')

# Agregando if else
listaPares = []
listaImpares = []
for numero in range(10):
    if numero % 2 ==0:
        listaPares.append(numero)

    else:
        listaImpares.append(numero)

print(f'Pares: {listaPares}')
print(f'Impares: {listaImpares}')

# El mismo ejercicio usando list comprehensions

listaPares = []
listaImpares = []
[listaPares.append(numero) if numero % 2 == 0 else listaImpares.append(numero) for numero in range(10)]
print(f'Pares: {listaPares}')
print(f'Impares: {listaImpares}')

# Lista de listas
listaListas = [[1,2,3],[4,5,6],[7,8,9,10]]
# Convertimos la lista de listas en una sola lista
listaSimple = [valor
               for sublista in listaListas
               for valor in sublista]
print(f'Lista simple: {listaSimple}')

# Ahora creamos una lista de numeros pares  a partir de la listaListas
# Sin list comprehensions, ciclos for anidados
listaPares = []
for sublista in listaListas:
    for valor in sublista:
        if valor % 2 == 0:
            listaPares.append(valor)

print(f'Resultado: {listaPares}')

# Con list comprehensions, en una sola linea de codigo
# No es necesario separar las lineas, solo es para mejor lectura de codigo
listaPares = []
listaPares = [valor for sublista in listaListas for valor in sublista if valor % 2 == 0]
print(f'Resultado: {listaPares}')