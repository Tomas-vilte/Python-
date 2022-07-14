# * Desempaquetar

numeros = [1,2,3]
print(numeros)
print(*numeros)
print(*numeros, sep=' - ')

# Desempaquetando al momento de pasar un parametro a una funcion
def sumar(a, b, c):
    print(f'Resultdo de la suma: {a + b + c}')

sumar(*numeros)

# Extraer algunas partes de una lista

miLista = [1,2,3,4,5,6]
a,*b,c,d = miLista
print(a,b,c,d)

# Unir listas

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = [lista1, lista2]
print(f'Lista de listas: {lista3} ')
lista3 = [*lista1, *lista2]
print(f'Unir lista: {lista3} ')

# Unir diccionarios

dic1 = {'A':1, 'B':2, 'C':3}
dic2 = {'D':4, 'E':5}

dict3 = {**dic1, **dic2}
print(f'Unir diccionarios: {dict3}')

# Construir una lista a partir de un str

lista = [*'HolaMundo']
print(lista)
print(*lista, sep='')