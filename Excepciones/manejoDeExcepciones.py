resultado = None

try:
    a = int(input('Ingrese un numero: '))
    b = int(input('Ingrese un numero: '))
    resultado = a/b

except ZeroDivisionError as e:
    print(f'ZeroDivisionError - Ocurrio un error: {e}, {type(e)}')   

except TypeError as e:
    print(f'TypeError - Ocurrio un error: {e}, {type(e)}')

except Exception as e:
    print(f'Ocurrio un error: {e}, {type(e)}')

print(f'Resultado: {resultado}')
print('Continuamos...')