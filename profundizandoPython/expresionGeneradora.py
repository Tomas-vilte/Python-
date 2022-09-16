import math
# Expresion generadora (Es un generador anonimo)
multiplicacion = (valor*valor for valor in range(4))
print(type(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))

# Tambien se puede pasar una expresion generadora a una funcion (sin parentisis)
suma = sum(valor*valor for valor in range(4))
print(f'Resultado de la suma: {suma}')