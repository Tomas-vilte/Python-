# Manejos de valores infinitos
import math
from decimal import Decimal


infinitoPositivo = float('inf')
#print(f'Infinito positivo:{infinitoPositivo}')
#print(f'Es infinito?: {math.isinf(infinitoPositivo)}')

infinitoNegativo = float('-inf')
#print(f'Infinito negativo:{infinitoNegativo}')
#print(f'Es infinito: {math.isinf(infinitoNegativo)}')


# Utilizando el modulo de math
infinitoPositivo = math.inf
#print(f'Infinito positivo:{infinitoPositivo}')
#print(f'Es inifinito?: {math.isinf(infinitoPositivo)}')

infinitoNegativo = -math.inf
#print(f'Infinito negativo:{infinitoNegativo}')
#print(f'Es infinito: {math.isinf(infinitoNegativo)}')

# Utilizando el moudelo decimal
infinitoPositivo = Decimal('Infinity')
print(f'Infinito positivo:{infinitoPositivo}')
print(f'Es inifinito?: {math.isinf(infinitoPositivo)}')

infinitoNegativo = Decimal('-Infinity')
print(f'Infinito negativo:{infinitoNegativo}')
print(f'Es infinito: {math.isinf(infinitoNegativo)}')


