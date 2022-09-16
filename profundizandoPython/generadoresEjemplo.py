# Generador de numeros del 1 al 5

def generadorDeNumeros():
    for numero in range(1,6):
        yield numero
        print('Se reanuda la ejecuccion de la funcion')

# Objecto generador
gen = generadorDeNumeros()
print(f'Objecto generador: {gen}')
print(type(gen))

# Consumimos los valores del generador
for valor in gen:
    print(f'Numero producido: {valor}')

# Consumir a demanda
gen = generadorDeNumeros()
try:
    print(f'Consumir a demanda: {next(gen)}')
except StopIteration as e:
    print(f'Error a consumir generador: {e}')

# Otra forma de consumir un generador
gen = generadorDeNumeros()
while True:
    try:
        valor = next(gen)
        print(f'Impresion del valor generado: {valor}')
    except StopIteration as e:
        print(f'Se termino de iterar el generador: {e}')
        break