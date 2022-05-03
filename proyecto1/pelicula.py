class peliculas:
    def __init__(self, nombre):
        self._nombre = nombre


    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self):
        return self._nombre

    def __str__(self):
        return f'Nombre de la pelicula: {self._nombre}'
