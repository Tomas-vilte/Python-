# Bool contiene los valores de True y False
# Tipos numericos, False para 0, True demas valores
numero1 = 0
resultado1 = bool(numero1)
print(f'Valor {numero1}, resultado: {resultado1}')

numero2 = 1
resultado2 = bool(numero2)
print(f'Valor {numero2}, resultado: {resultado2}')

# Tipo str, false para '', True demas valores

cadena1 = ''
resultado3 = bool(cadena1)
print(f'Valor {cadena1}, resultado: {resultado3}')

cadena2 = 'hola'
resultado4 = bool(cadena2)
print(f'Valor {cadena2}, resultado: {resultado4}')

# Tipo colecciones, False para colecciones vacias, True para todas las colecciones
# Lista

lista1 = []
resultado5 = bool(lista1)
print(f'Valor {lista1}, resultado: {resultado5}')

lista2 = ['Buenas']
resultado6 = bool(lista2)
print(f'Valor {lista2}, resultado: {resultado6}')

# Tupla

tupla1 = ()
resultado6 = bool(tupla1)
print(f'Valor {tupla1}, resultado: {resultado6}')

tupla2 = (2,3,4)
resultado7 = bool(tupla2)
print(f'Valor {tupla2}, resultado: {resultado7}')

# Diccionario

diccionario1 = {}
resultado8 = bool(diccionario1)
print(f'Valor {diccionario1}, resultado: {resultado8}')

diccionario2 = {'Edad': 18}
resultado9 = bool(diccionario2)
print(f'Valor {diccionario2}, resultado: {resultado9}')

if bool('asd'):
    print('Regreso verdadero')
else:
    print('Regreso falso')

variable = 10

while variable:
    print('Ejecuccion ciclo while')
    break
else:
    print('Fin del ciclo')

