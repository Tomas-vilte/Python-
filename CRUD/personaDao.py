from loggerBase import log
from persona import Persona
from conexion import conexion


class personaDAO:
    _SELECIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona (nombre, apellido, email,) VALUES (%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'

    @classmethod
    def seleccionar(cls):
        with conexion.obtenerCursor() as cursor:
            cursor.execute(cls._SELECIONAR)
            registroRecuperados = cursor.fetchall()
            personas = []
            for registro in registroRecuperados:
                print(f'Registros recuperados: {registroRecuperados}')
                persona = Persona(registro[0], registro[1], registro[2], registro[3])
                personas.append(persona)
            return personas


    
    @classmethod
    def insertar(cls, persona):
        with conexion.obtenerConexion() as conexion:
            with conexion.obtenerCursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'Persona a insertar: {persona}')
                return cursor.rowcount






if __name__ == '__main__':
    #Insertar un registro
    persona1 = Persona(nombre='Ali', apellido='Vilte', email='Alivilte@gmail.com')
    personasInsertadas = personaDAO.insertar(persona1)
    log.debug(f'Personas insertadas: {personasInsertadas}')
    
    personas = personaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)