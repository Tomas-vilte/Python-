from Monitor import Monitor
from Teclado import Teclado
from Raton import Raton


class Computadora():
    contadorComputadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contadorComputadoras += 1
        self._idComputadoras = Computadora.contadorComputadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    @property
    def idComputadoras(self):
        return self._idComputadoras

    @idComputadoras.setter
    def idComputadoras(self):
        return self._idComputadoras

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self):
        return self._nombre

    @property
    def monitor(self):
        return self._monitor

    @monitor.setter
    def monitor(self):
        return self._monitor

    @property
    def teclado(self):
        return self._teclado

    @teclado.setter
    def teclado(self):
        return self._teclado

    @property
    def raton(self):
        return self._raton
    
    @raton.setter
    def raton(self):
        return self._raton

    def __str__(self):
        return f'''
        {self._nombre}, {self._idComputadoras}
        Monitor: {self._monitor}
        Teclado: {self._teclado}
        Raton: {self._raton}
        
        '''



Monitor1 = Monitor('Samsung', '27 Pulgadas')
Teclado1 = Teclado('Usb', 'Logitech')
Raton1 = Raton('Bluetooh', 'Redragon')
Computadora1 = Computadora('Hp', Monitor1, Teclado1, Raton1)
print(Computadora1)
