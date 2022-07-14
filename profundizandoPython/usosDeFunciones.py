# Las funciones en python son ciudadanas de primera clase
# First class citizens

# Definimos la funcion

def sumar(a, b):
    return a + b

#1. Asignar una funcion a una variable (no se usan parentesis)
miFuncion = sumar

# Verificar el tipo de la variable
print(type(miFuncion))

# Llamamos la funcion a traves de la variable
resultado = miFuncion(5, 8)
print(f'Resultado: {resultado}')

#2. Funcion como argumento
def operacion(a, b, sumar_arg):
    print(f'Resultado sumar: {sumar_arg(a, b)}')

operacion(4, 5, sumar)

#3. Podemos retornar una funcion
def retornarFuncion():
    # Retornamos una funcion
    return sumar

miFuncionRetornada = retornarFuncion()
print(f'Resultado de la funcion retornada: {miFuncionRetornada(5, 7)}')