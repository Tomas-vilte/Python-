class Empleado:
    def __init__(self, nombre, sueldo):
        self._nombre = nombre
        self._sueldo = sueldo

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self):
        return self._nombre

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self):
        return self._sueldo

    def __str__(self):
        return f'Empleado: [Nombre: {self._nombre}, Sueldo: {self._sueldo}]'

    def mostrar_detalles(self):
        return self.__str__()