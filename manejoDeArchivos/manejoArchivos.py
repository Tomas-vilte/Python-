class manejoArchivos:
    def __init__(self, nombre):
        self.nombre = nombre

    def __enter__(self):
        print('Obetenemos el recurso'.center(50, '-'))
        self.nombre = open(self.nombre, 'r', encoding='utf8')
        return self.nombre

    def __exit__(self, tipoExcepcion, valorExcepcion, trazaError):
        print('Cerramos el recurso'.center(50, '-'))
        if self.nombre:
            self.nombre.close() 