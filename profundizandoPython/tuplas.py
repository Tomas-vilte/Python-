# Profundizando en tuplas

# Declarar variables

a, b = 'Hola', 'Adios'
print(a, b)
# Swap (intercambio)
a, b = b, a
print(a, b)

# Regresar multiples valores en una funcion
def minmax(elementos):
    return min(elementos), max(elementos)

min, max =minmax([1,2,3,4,5])
print(f'Valor minimo: {min}, Valor maximo: {max}')

# Regresar la suma de una tupla

resultado = sum((1,2,3,4,5))
print(f'Resultado: {resultado}')

def sumar(*args):
    return sum(args)

resultado = sumar(1,2,3,4,5,6)
print(f'Resultado: {resultado}')