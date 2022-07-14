from urllib.request import urlopen

# Leer contenido online

with urlopen('file:///home/tomi/Descargas/02-18-00-LeerArchivoOnline-UP/nuevo_archivo.txt') as mensaje:
    contenido = mensaje.read().decode('UTF-8')

# Contar ocurrencias de una cadena
print(contenido.count('Universidad'))

# Upper convierte a mayusculas un str
print(contenido.upper())

# Lower convierte a minusculas un str
print(contenido.lower())

# Buscamos la cadena python en el contenido
print('Existe python?:', 'python'.lower() in contenido.lower())
print('Existe python?:', 'python'.upper() in contenido.upper())

# startswith - inicia con
print('Inicia con:', contenido.startswith('En GlobalMentoring.com.mx'))

# endswith - termina con
print('Termina con:', contenido.endswith('GlobalMentoring.com.mx'))

mensaje = 'Hola Mundo'
print(mensaje.lower().islower())
print(mensaje.upper().isupper())

# Alinear cadenas

# Centrar un str
titulo = 'Sitio web de GlobalMentoring.com.mx'
#print(titulo.center(50, '*'))
#print(len(titulo.center(50, '*')))
print(titulo.center(len(titulo)+10, '-'))

# ljust - Alinea a la izquierda
#print(titulo.ljust(50, '*'))
print(titulo.ljust(len(titulo)+10, '-'))

# rjust - Alinea a la derecha
print(titulo.rjust(50, '-'))
print(titulo.rjust(len(titulo)+10, '-'))

# Reemplazar contenido en un str
print(contenido.replace(' ', '-'))

# Eliminar caracteres al inicio y final de un str - strip
titulo = ' *** GlobalMentoring.com.mx *** '
print('Titulo original:', titulo, len(titulo))
titulo = titulo.strip()
print('Cadena modificada:', titulo, len(titulo))
titulo = '***GlobalMentoring.com.mx***'.strip('*')
print('Cadena modificada:', titulo)
titulo = '***GlobalMentoring.com.mx***'.lstrip('*')
print('Cadena modificada:', titulo)
titulo = '***GlobalMentoring.com.mx***'.rstrip('*')
print('Cadena modificada:', titulo)

titulo = ' *** GlobalMentoring.com.mx '.strip().strip('*').strip()
print('Cadema modificada:', titulo)