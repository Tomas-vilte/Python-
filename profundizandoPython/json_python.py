# Leer archivo json
# JSON  = JavaScript Object Notation
import urllib.request

respuesta = urllib.request.urlopen('http://globalmentoring.com.mx/api/personas.json')
print(respuesta)

cuerpo_repuesta = respuesta.read()
print(cuerpo_repuesta)

