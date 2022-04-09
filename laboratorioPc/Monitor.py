class Monitor():
    contadorMonitores = 0
    
    def __init__(self, marca, tamaño):
        Monitor.contadorMonitores += 1
        self._idMonitor = Monitor.contadorMonitores
        self._marca = marca
        self._tamaño = tamaño

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self):
        return self._marca

    @property
    def tamaño(self):
        return self._tamaño

    @tamaño.setter
    def tamaño(self):
        return self._tamaño

    @property
    def idMonitor(self):
        return self._idMonitor

    @idMonitor.setter
    def idMonitor(self):
        return self._idMonitor
    
    def __str__(self):
        return f'ID: {self._idMonitor}, Marca: {self._marca}, Tamaño: {self._tamaño}'


if __name__ == '__main__':
    monitores = Monitor('Samsung', 27)  
    print(monitores)
    monitores2 = Monitor('Asus', 28)
    print(monitores2)