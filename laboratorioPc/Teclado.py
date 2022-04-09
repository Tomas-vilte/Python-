from dispositivoEntrada import dispositivoEntrada

class Teclado(dispositivoEntrada):
    contadorTeclados = 0
    
    def __init__(self, tipo_entrada, marca):
        Teclado.contadorTeclados += 1
        self._idteclado = Teclado.contadorTeclados
        super().__init__(tipo_entrada, marca)

    def __str__(self):
        return f'ID: {self._idteclado}, {super().__str__()}'


if __name__ == '__main__':
    teclado1 = Teclado('USB', 'Redragon')
    print(teclado1)
    teclado2 = Teclado('Bluetooh', 'Genius')
    print(teclado2)