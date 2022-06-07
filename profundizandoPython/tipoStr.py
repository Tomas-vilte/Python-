# Profundizando en el tipo str

# help(str.capitalize)

#help(str.join)

'''
tuplaStr = 'Hola', 'Mundo', 'Universidad', 'Python'
mensaje = ' '.join(tuplaStr)
print(f'Mensaje {mensaje}')

listaCursos = 'Java', 'Python', 'Angular', 'Spring'
mensaje2 = ', '.join(listaCursos)
print(f'Mensaje {mensaje2}')

cadena = 'HolaMundo'
mensaje3 = '.'.join(cadena)
print(f'Mensaje: {mensaje3}')

diccionario = {'Nombre': 'Alexis', 'Apellido': 'Vilte', 'Edad': '23'}
llaves = '-'.join(diccionario.keys())
valores = '-'.join(diccionario.values())
print(f'Llaves: {llaves}')
print(f'Valores: {valores}')


#help(str.split)

#cursos = 'Java Python JavaScript Angular Spring Excel'
#listaCursos = cursos.split()
#print(f'Mensaje: {listaCursos}')

'''



#cursosSeparadosPorComa = 'Java, Python, JavaScript, Angualar, Spring, Execl'
#listaCursos1 = cursosSeparadosPorComa.split(',')
#print(f'Mensaje: {listaCursos1}')
#print(len(listaCursos1))

#listaCursos = cursosSeparadosPorComa.split(', ', 3)
#print(f'Lista cursos: {listaCursos}')
#print(len(listaCursos))

# Dar formato a un str


nombre = 'Juan'
edad = 28
sueldo = 3000
mensajeConFormato = f'Nombre: {nombre} Edad: {edad} Sueldo: {sueldo}'


mensajeConFormato1 = 'Nombre {} Edad {} Sueldo {:.2f} '.format(nombre, edad, sueldo)
print(mensajeConFormato1)

mensajeConFormato2 = 'Nombre  {0} Edad {1} Sueldo {2:.2f}'.format(nombre, edad, sueldo)
print(mensajeConFormato2)

mensajeConFormato3 = 'Edad {1} Sueldo {2} Nombre {0}'.format(nombre, edad, sueldo)
print(mensajeConFormato3)

mensajeConFormato4 = 'Nombre {n} Edad {e} Sueldo {s:.2f}'.format(n=nombre, e=edad, s=sueldo)
print(mensajeConFormato4)

diccionario = {'nombre':'Ivan', 'edad':23, 'sueldo':3000.00}
mensajeConFormato5 = 'Nombre {persona[nombre]} Edad {persona[edad]} Sueldo {persona[sueldo]:.2f}'.format(persona=diccionario)
print(mensajeConFormato5)

# Metodo print

print(nombre, edad, sueldo, sep=', ')

# Multiplacacion str

resultado = 3*'Hola'
print(f'Resultado: {resultado}')


# Multiplicacion tuplas
resultado = 5*('Hola', 10,)
print(f'Resultado: {resultado}')

# Multiplicacion listas

resultado = 10*[0]
print(f'Resultado: {resultado}')

# Caracteres de escape

resultado = 'Hola, \' mundo'
print(f'Resultado: {resultado}')

resultado = 'Se va a eliminar el punto.\b\b\b'
print(f'Resultado: {resultado}')

# Caracter \

resultado = 'c:\\nuevo\\Juan'
print(f'Resultado: {resultado}')

# raw string

resultado = r'Cadena con \n salto de linea'
print(f'Resultado: {resultado}')

# Caracteres unicode

print('Hola\u0020Mundo')
print('Notacion simple de unicode:', '\u0041')
print('Notacion extendia:', '\U00000041')
print('Notacion hexdecimal:', '\x41')
print('Corazon:', '\u2665')
print('Cara soriendo:', '\U0001f600')
print('Serpiente:', '\U0001F40D')

# Caracteres ascii

caracter = chr(65)
print('A Mayuscula:', caracter)

caracter = chr(64)
print('Simbolo @:', caracter)

caracter = chr(97)
print('a minuscula:', caracter)