# Decoradores
# Un decorador es una funcion que recibe una funcion y regresa otra
# Lo utilizamos para extender funcionalidad
#1. Funcion decorador (a)
#2. Funcion a decorar (b)
#3. Funcion decorada (c)

def funcionDecoradorA(funcionADecorarB):
    def funcionDecoradaC(*args, **kwargs):
        print('Antes de ejecutar la funcion decorada c')
        resultado = funcionADecorarB(*args, **kwargs)
        print('Despues de ejecutar la funcion')
        return resultado

    return funcionDecoradaC


@funcionDecoradorA
def sumar(a,b):
    return a + b

resultado = sumar(5,6)
print('Resultado de la suma', resultado)