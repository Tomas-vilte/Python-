from numerosIdenticos import numerosIdenticos

resultado = None

try:
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    if a == b:
        raise numerosIdenticos("Numeros identicos")
    resultado = a/b
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - Ocurrio un error: {e}, {type(e)}')

except TypeError as e:
    print(f'TypeError - Ocurrio un error: {e}, {type(e)}')

except Exception as e:
    print(f'Excepction - Ocurrio un error: {e}, {type(e)}')

else:
    print('No se arrojo ninguna excepcion')
finally:
    print('Ejecucion del bloque finally')