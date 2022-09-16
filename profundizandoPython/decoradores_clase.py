# Decoradores de clase
# Permiten transformar de manera programatica nuestra clase
# Es similar a los decoradores de funciones (es metaprogramacion)
import inspect


def decorador_repr(cls):
    print('Se ejecuta decorador')
    print(f'Recibimos el objecto de la clase: {cls.__name__}')
    # Revisamos los atributos de la clase con el metodo vars
    atributos = vars(cls)
    # Iteramos cada atributo
    # for nombre, atributo in atributos.items():
    # print(nombre, atributo)

    # Revisamos si se ha sobreescrito el metodo __init__

    if '__init__' not in atributos:
        raise TypeError(f'{cls.__name__} no ha sobreescrito el metodo __init__')

    firma_init = inspect.signature(cls.__init__)
    print(f'Firma metodo __init__: {firma_init}')
    # Recuperamos los parametros, excepto el primero que es self
    parametros_init = list(firma_init.parameters)[1:]
    print(f'Parametros init: {parametros_init}')

    # Revisamos si cada parametro tiene un metodo property asocidado
    for parametro in parametros_init:
        # Property es un valor de tipo built-in para preguntar si
        # se está utilizando el decorador property
        es_metodo_property = isinstance(atributos.get(parametro), property)
        if not es_metodo_property:
            raise TypeError(f'No existe un metodo property para el parametro: {parametro}')

    # Crear el metodo repr dinamicamente
    def metodo_repr(self):
        # Obtenemos el nombre de la clase dinamicamente
        nombre_clase = self.__class__.__name__

        # Obtenemos los nombres de las propiedades y sus valores dinamicamente
        # Expresion generadora, crear nombre_atr=valor_atr
        generador_arg = (f'{nombre}={getattr(self, nombre)!r}' for nombre in parametros_init)
        # Lista del generador
        lista_arg = list(generador_arg)
        print(f'Lista del generador: {lista_arg}')
        # Creamos la cadena a partir de la lista de argumentos
        argumentos = ', '.join(lista_arg)
        print(f'Argumentos del metodo repr: {argumentos}')
        # Creamos la forma del metodo __repr__, sin su nombre,
        resultado_metodo_repr = f'{nombre_clase}({argumentos})'
        print(f'Resultado metodo repr: {resultado_metodo_repr}')
        return resultado_metodo_repr

    # Agregar dinamicamente el metodo repr a nuestra clase
    setattr(cls, '__repr__', metodo_repr)

    return cls


@decorador_repr
class Persona:
    def __init__(self, nombre, apellido, edad):
        print('Se ejecuta el inicializador')
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    @property
    def edad(self):
        return self._edad

    # def __repr__(self):
    # return f'Persona({self._nombre}, {self._apellido})'


persona1 = Persona('Juan', 'Perez', 20)
print(persona1)
persona2 = Persona('Carla', 'Gomez', 22)
print(persona2)
# Tiene los metodos de propiedad nombré, apellido, edad, repr
print(dir(Persona))
# Tiene el metodo repr sobreescrito
codigo_repr = inspect.getsource(persona1.__repr__)
print(codigo_repr)
