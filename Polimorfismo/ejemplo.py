class coche():
    def desplazamiento(self):
        print('Me desplazo en 4 ruedas')


class moto():
    def desplazamiento(self):
        print('Me desplazo en 2 ruedas')


class camion():
    def desplazamiento(self):
        print('Me desplazo en 6 ruedas')

def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()

miVehiculo=moto()

desplazamientoVehiculo(miVehiculo)

