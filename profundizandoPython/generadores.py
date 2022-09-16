# Generadores
# Es una funcion especial, retorna una secuencia de valores
# Suspende la ejecucion de la funcion yield (producir) (no se usa return)

def generador():
    yield 1
    yield 2
    yield 3

# Consumimos el generador a demanda
gen = generador()
# Con cada llamada consumimos un valor
print(next(gen))
print(next(gen))
print(next(gen))


# Si tratamos de consumir mas valores de los que produce el generador
# lanza un error de StopIteration
#print(next(gen))

# Consumiendo los valores del generador con un ciclo for

for valor in generador():
    print(f'Numero generado: {valor}')

print(type(gen))
