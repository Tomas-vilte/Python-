from dispositivoEntrada import dispositivoEntrada

class Raton(dispositivoEntrada):
    contadorRatones = 0
    
    def __init__(self, tipo_entrada, marca):
        Raton.contadorRatones += 1
        self._idraton = Raton.contadorRatones
        super().__init__(tipo_entrada, marca)

    def __str__(self):
        return f'ID: {self._idraton}, {super().__str__()}'


if __name__ == '__main__':
    raton1 = Raton('USB', 'Genius')
    print(raton1)
    raton2 = Raton('Bluetooh', 'Logitech')
    print(raton2)

