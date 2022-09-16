# Orden de inicializacion de objetos

class Padre:
    def __init__(self):
        print('Inicializador padre')

    def metodo(self):
        print('Metodo padre')

class hijo(Padre):
    # Se manada a llamar el metodo __init__ de la clase padre
    # siempre y cuando la clase hija no defina su propio metodo init

    # Definimos el metodo init
    def __init__(self):
        # De manera opcional podemos llamar al metodo __init__ de la clase padre (super )

        print('Inicializador hijo')
        super().__init__()

    # Sobreescribimos el metodo heredado de la clase padre
    def metodo(self):
        print('Metodo sobreescrito hijo')
        super().metodo()

#padre1 = Padre()
#padre1.metodo()

hijo = hijo()
hijo.metodo()