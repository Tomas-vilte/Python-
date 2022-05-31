from loggerBase import log
from conexion import Conexion


class cursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug(f'inicio del metodo with __enter__')
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, typeExcept, valueExcepction, traceBackException):
        log.debug('Se ejecuta metodo __exit__')
        if valueExcepction:
            self._conexion.rollback()
            log.error(f'Ocurrio una excepcion: {valueExcepction}, {typeExcept}, {traceBackException}')
        else:
            self._conexion.commit()
            log.debug('Commit de la transaccion')
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)

if __name__ == '__main__':
    with cursorDelPool() as cursor:
        log.debug('Dentro del bloque with')
        cursor.execute('SELECT * FROM persona')
        log.debug(cursor.fetchall())
