#with open('prueba.txt', 'r', encoding='utf8') as archivo:
from manejoArchivos import manejoArchivos


with manejoArchivos('prueba.txt') as archivo:
    print(archivo.read())

    