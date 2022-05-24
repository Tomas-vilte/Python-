from loggerBase import log

class persona:

    def __init__(self, idPersona=None, nombre=None, apellido=None, email=None):
        
        self._idPersona = idPersona
        self._nombre = nombre
        self._apellido = apellido
        self._email = email

    def __str__(self):
        return f'''
        ID: {self._idPersona}, Nombre: {self._nombre}, 
        Apellido: {self._apellido}, Correo: {self._email}
        '''

    @property
    def idPersona(self):
        return self._idPersona

    @idPersona.setter
    def idPersona(self, idPersona):
        self.idPersona = idPersona

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

if __name__ == '__main__':
    persona1 = persona(1, 'Joan', 'Herrera', 'Joanherrera@gmail.com')
    log.debug(persona1)
    # Simular un insert 
    persona1 = persona(nombre='Alexis', apellido='Vilte', email='Alexisvilte@gmail.com')
    log.debug(persona1)
    # Simular un delete
    persona1 = persona(idPersona=1)
    log.debug(persona1)