from cursorDelPool import cursorDelPool
from loggerBase import log
from persona import Persona
from conexion import Conexion


class personaDAO:
    _SELECIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona (nombre, apellido, email) VALUES (%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'

    @classmethod
    def seleccionar(cls):
        with cursorDelPool() as cursor:
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
        with cursorDelPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Persona a insertar: {persona}')
            return cursor.rowcount


    @classmethod
    def actualizar(cls, persona):
        with cursorDelPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email, persona.idPersona)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Registro actualizado {persona}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, persona):
        with cursorDelPool() as cursor:
            valores = (persona.idPersona,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Registro eliminado: {persona}')
            return cursor.rowcount


if __name__ == '__main__':
    #Insertar un registro
    persona1 = Persona(nombre='Belen', apellido='Vilte', email='Belenvilte@gmail.com')
    personasInsertadas = personaDAO.insertar(persona1)
    log.debug(f'Personas insertadas: {personasInsertadas}')
    
    #Actualizar un registro
    #persona2 = Persona(4, 'Belen', 'Vilte', 'Belenvilte@gmail.com')
    #personaActualizada = personaDAO.actualizar(persona2)
    #log.debug(f'Personas actualizadas: {personaActualizada}')

    #Eliminar un registro
    #persona3 = Persona(idPersona=4)
    #personaEliminada = personaDAO.eliminar(persona3)
    #log.debug(f'Registro eliminado: {personaEliminada}')

    #Seleccionar 
    #personas = personaDAO.seleccionar()
    #for persona in personas:
        #log.debug(persona)