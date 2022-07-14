from pprint import pprint as pp

# Profundizando en diccionarios

# Los diccionarios guardan un orden (a diferencia de un set)
diccionario = {'Nombre':'Juan', 'Apellido':'Perez', 'Edad':28}
print(diccionario)

# Los diccionarios son mutables, pero las llaves deben ser inmutables
#diccionario = {[1,2]:'valor1'}

#diccionario = {(1,2):'Valor1'}
#print(diccionario)

# Se agrega una llave si no se encuentra
diccionario['Departamento'] = 'Sistemas'
print(diccionario)

# No hay valores duplicados en las llaves de un diccionario (si ya existe se reemplaza)
diccionario['Nombre'] = 'Juan carlos'
print(diccionario)

# Recuperar un valor indicando una llave
print(diccionario['Nombre'])
# Si no encuentra la llave lanza una excepcion
#print(diccionario['nombre'])

# Metodo get recupera una llave, y si no existe NO lanza excepcion
# ademas podemos regresar un valor en caso de que no exista la llave
print(diccionario.get('Nombresa', 'No se encontro la llave'))

# setdefault si modifica el diccionario, ademas de agregar un valor por default
nombre = diccionario.setdefault('Nombres', 'Valor por default')
print(nombre)
print(diccionario)

# imprimir con pprint
#help(pp)

pp(diccionario, sort_dicts=False)