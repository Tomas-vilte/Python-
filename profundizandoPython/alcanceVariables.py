# Alcance de variables (scope)

varGlobal = 'Variable global'

def imprimir():
    # Acceder a una variable global
    global varGlobal
    print(f'Variable global desde funcion: {varGlobal}')
    # Definicion de variable local
    varLocal = 'Variable local'
    print(f'Variable local desde funcion: {varLocal}')
    varGlobal = 'Nuevo valor variable global'

    def funcionAnidada():
        print(f'Variable local dentro de funcion anidada {varLocal}')

    funcionAnidada()

imprimir()
print(f'Var global fuera de funcion: {varGlobal}')
# No es posible acceder a variables locales fuera
# del bloque donde se definieron
#print(f'Var local fuera de la funcion: {varLocal}')
