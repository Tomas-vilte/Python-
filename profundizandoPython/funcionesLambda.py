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

# Funcion lambda que no recibe argumentos (Debemos regresar una expresion valida )

miFuncionLambda = lambda: 'Funcion sin argumentos'
print(f'Llamar funcion lambda sin argumentos: {miFuncionLambda()}')

# Funcion lambda con paramentros por default
miFuncionLambda = lambda a=2, b=3: a + b
print(f'Resultado de argumentos por default: {miFuncionLambda()}')

# Funcion lambda con argumentos variables *args y **kwargs

miFuncionLambda = lambda *args, **kwargs: len(args) + len(kwargs)
print(f'Resultado de argumentos variables: {miFuncionLambda(1,2,3, a=5, b=6)}')

# Funciones lambda con argumentos variables y valores por default
miFuncionLambda = lambda a,b, c=3,*args, **kwargs: a+b+c+len(args)+len(kwargs)
print(f'Resultado de la funcion lamda: {miFuncionLambda(1,2,4, 5,6,7,e=5, f=7)}')