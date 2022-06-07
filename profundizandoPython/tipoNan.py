import math
from decimal import Decimal
# NaN - Not a numbre (No es un numero)
# NaN no es sensible a mayusculas y minusculas
# NaN es un tipo de dato numero indefinido

a = float('NaN')
print(f'a:{a}')
print(f'Es NaN (not a number)?: {math.isnan(a)} ')

a1 = Decimal('NaN')
print(f'a1: {a1}')
print(f'Es NaN (not a number)?: {math.isnan(a1)} ')