from Polimorfismo.Gerente import Gerente
from Polimorfismo.Empleado import Empleado


def imprimir_detalles(objecto):
    #print(objecto)
    print(type(objecto))
    print(objecto.mostrar_detalles())
    if isinstance(objecto, Gerente):
        print(objecto.departamento)

empleado = Empleado('Juan', 5000)
imprimir_detalles(empleado)

gerente = Gerente('Carla', 5000, 'Sistemas')
imprimir_detalles(gerente)  