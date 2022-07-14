# Funciones lambda
# Son funciones anonimas y son pequeñas (una linea de codigo)
# No es posible funcion a una variable
#miFuncion =def sumar(a, b): return a + b

# Con una funcion lambda (anonima, sin nombre, y una sola linea)
# No se necesita agregar parentesis para los paramentros
# No se necesita usar la palabar return, pero si debe regresar una expresion

miFuncionLambda = lambda a, b: a + b

resultado = miFuncionLambda(5, 5)
print(f'Resultado de sumar con funcion lambda: {resultado}')