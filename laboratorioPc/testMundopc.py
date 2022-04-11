from Computadora import Computadora
from Monitor import Monitor
from Orden import Orden
from Raton import Raton
from Teclado import Teclado


Monitor1 = Monitor('Samsung', '27 Pulgadas')
Teclado1 = Teclado('Usb', 'Logitech')
Raton1 = Raton('Bluetooh', 'Redragon')
Computadora1 = Computadora('Hp', Monitor1, Teclado1, Raton1)


Monitor2 = Monitor('Aoc', '27 Pulgadas')
Teclado2 = Teclado('Usb', 'Razer')
Raton2 = Raton('Bluetooh', 'Noga')
Computadora2 = Computadora('Acer', Monitor2, Teclado2, Raton2)

Monitor3 = Monitor('Samsung', '27 Pulgadas')
Teclado3 = Teclado('Usb', 'Genius')
Raton3 = Raton('Usb', 'Redragon')
Computadora3 = Computadora('Gamer', Monitor3, Teclado3, Raton3)

computadoras1 = [Computadora1, Computadora2]
Orden1 = Orden(computadoras1)
print(Orden1)
Orden1.agregarComputadoras(Computadora3)
print(Orden1)