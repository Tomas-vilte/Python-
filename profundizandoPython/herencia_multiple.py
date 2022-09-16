# Ejemplo de herencia simple
class listaSimple:
    def __init__(self, elementos):
        self._elementos = list(elementos)

    def agregar(self, elemento):
        self._elementos.append(elemento)

    def __getitem__(self, indice):
        return self._elementos[indice]

    def ordenar(self):
        self._elementos.sort()

    def __len__(self):
        return len(self._elementos)

    def __repr__(self):
        return f'{self.__class__.__name__}({self._elementos!r})'


class listaOrdenada(listaSimple):
    def __init__(self, elementos=[]):
        super().__init__(elementos)
        # Ordenamos siempre los elementos una vez inicializados
        self.ordenar()

    def agregar(self, elemento):
        super().agregar(elemento)
        # Ordenamos el nuevo elemento
        self.ordenar()


# Lista solo acepta numeros
class listaEnteros(listaSimple):
    def __init__(self, elementos=[]):
        for elemento in elementos:
            self._validar(elemento)
        # Una vez validados los elementos, los agregamos
        super().__init__(elementos)

    def _validar(self, elemento):
        # Validamos si el elemento es de tipo entero
        if not isinstance(elemento, int):
            raise ValueError(f'No es un valor entero: {elemento}')

    # Sobreescribimos el metodo agregar de la clase padre
    def agregar(self, elemento):
        self._validar(elemento)
        # Una vez validado lo agregamos a la lista
        super().agregar(elemento)


# Lista de enteros ordenada
class ListaEnterosOrdenada(listaEnteros, listaOrdenada):
    def __init__(self, elementos=[]):
        super().__init__(elementos)


listaSimple1 = listaSimple([5, 3, 7, 9])
print(listaSimple1)

lista_ordenada = listaOrdenada([4, 3, 6, 9, 10, -1])
print(lista_ordenada)
lista_ordenada.agregar(-14)
print(lista_ordenada)
print(len(lista_ordenada))

lista_enteros = listaEnteros([1, 2, 3])
print(lista_enteros)

# Lista enteros ordenada
lista_enteros_ordenada = ListaEnterosOrdenada([20,4,5,-1,10,14,-4])
print(lista_enteros_ordenada)
lista_enteros_ordenada.agregar(-20)
print(ListaEnterosOrdenada)

#Saber la clase padre y su orden
#print(lista_enteros_ordenada.__bases__)
# MRO (Method resolution Order)
#print(lista_enteros_ordenada.__mro__)

# isintance
print('Es entero?', isinstance(10, int))
print('Es una cadena', isinstance('Hola', str))
print('Es una lista de enteros ordenada', isinstance(lista_enteros_ordenada, ListaEnterosOrdenada))
print('Es lista entero?', isinstance(lista_enteros_ordenada, listaEnteros))
print('Es una lista ordenada?', isinstance(lista_enteros_ordenada, listaOrdenada))
print('Es lista simple', isinstance(lista_enteros_ordenada, listaSimple))
print('Es object', isinstance(lista_enteros_ordenada, object))
print('Es de varios tipos?', isinstance(lista_enteros_ordenada, (listaEnteros, listaSimple)))