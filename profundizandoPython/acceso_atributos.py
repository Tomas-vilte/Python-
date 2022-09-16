# Ejemplo atributos publicos, protegidos, privados

class Miclase:
    def __init__(self, publico, protegido, privado):
        self.publico = publico
        self._protegido = protegido
        self.__privado = privado

objecto = Miclase('Valor publico', 'Valor protegido', 'Valor privado')
# Acceso al atributo publico
print(objecto.publico)
# Modificar el valor publico
objecto.publico = 'Nuevo valor publico'
print(objecto.publico)

# Acceso al valor protegido
# Solo dentro de la misma clase o clases hijas
print(objecto._protegido)
objecto._protegido = 'Nuevo valor protegido'
print(objecto._protegido)

# Acceder al valor privado
#print(objecto.__privado)
# Pero, convierte: objecto._clase__atributo_privado
print(objecto._Miclase__privado)
# Modificar el valor privado
objecto._Miclase__privado = 'Nuevo valor privado'
print(objecto._Miclase__privado)