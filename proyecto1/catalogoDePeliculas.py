import os
from pelicula import peliculas


class catalogoDePeliculas(peliculas):
    rutaArchivo = 'pelicula.txt'

    @classmethod

    def agregarPelicula(cls, pelicula):
        with open(cls.rutaArchivo, 'a', encoding='utf8') as archivo:
            archivo.write(f'{pelicula.nombre}\n')
    
    @classmethod
    def listarPeiliculas(cls):
        with open(cls.rutaArchivo, 'r', encoding='utf8') as archivo:
            print(f'Catalogo de peliculas'.center (50, '-'))
            print(archivo.read())

    @classmethod
    def eliminarPelicula(cls):
        os.remove(cls.rutaArchivo)
        print('Archivo eliminado: {cls.rutaArchivo}')
