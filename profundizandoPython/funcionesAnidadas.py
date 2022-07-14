# Funciones Anidadads

def calculadora(a, b, operacion='Sumar'):
    #1. Definir Funcion anidada
    def sumar(a, b):
        return a + b

    def restar(a, b):
        return a - b

    #2. Llamamos a la funcion anidada
    if operacion == 'sumar':
        print(f'Resultado sumar: {sumar(a, b)}')
    elif operacion == 'restar':
        print(f'Resultado restar: {restar(a, b)}')

calculadora(5, 6, operacion='sumar')
calculadora(4, 3, operacion='restar')