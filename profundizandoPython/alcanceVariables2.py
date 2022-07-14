# Mas funciones anidadas y alcance de variables

def funcionExterna():
    variableLocalExterna = 'Variable local externa'

    def funcionAnidada():
        variableLocalAnidada = 'Variable local anidada'
        nonlocal variableLocalExterna
        variableLocalExterna = 'Nuevo valor variable local externa'

    funcionAnidada()

    print(f'Valor variable local externa: {variableLocalExterna}')
    # No es posible acceder a una variable local mas interna
    # print(f'Valor variable local externa: {variableLocalExterna}')

funcionExterna()