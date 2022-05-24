from persona import persona
from conexion import conexion


class personaDAO:
    _SELECIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona (nombre, apellido, email,) VALUES (%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'

    @classmethod
    def seleccionar(cls):
        cursor = conexion.obtenerCursor()
        cursor.execute(cls._SELECIONAR)