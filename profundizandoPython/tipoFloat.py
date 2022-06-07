# Profundizando tipo float
a = 3.0
print(f'a:{a:.2f}')

# Constructor float puede recibir int y str
b = float('10')
print(f'b:{b:.2f}')
b1 = float(10)
print(f'b1:{b1:.2f}')

# Notacion exponencial (valores postivos y negativos)
c = 3e5
print(f'c1:{c:.2f}')
c1 = 3e-5
print(f'c:{c1:.5f}')

# Cualquier calculo que involucre un flota, se promueve a float

d = 4.0 + 5
print(f'd:{d}')
print(type(d))