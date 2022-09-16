# Un closure es una funcion que define a otra, y ademas la puede regresar
# La funcion anidada puede acceder a la variables locales definidas
# En la funcion principal o externa

# Funcion principal

# def operacion(a,b):
     #Definimos una funcion interna o anidada
#        def sumar():
#        return a + b

    # Retornar la funcion
#    return sumar

# Funcion principal
def operacion(a,b):
    #1. Definimos una funcion lambda interna o anidada y la retornamos
    return lambda: a + b

mifuncion = operacion(2,5)
print(f'Resultado de la funcion closure: {mifuncion()}')

# Llamar la funcion regresada al vuelo
print(f'Resultado de la funcion closure al vuelo: {operacion(2,3)()}')