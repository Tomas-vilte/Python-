from loggerBase import log
import psycopg2 
import sys


class conexion:
    _dataBase = 'postgres'
    _userName = 'postgres'
    _password = 'postgres'
    _dbPort = '5432'
    _host = 'localhost'
    _conexion = None
    _cursor = None

    @classmethod
    def obtenerConexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion = psycopg2.connect(host=cls._host,
                                                user=cls._userName,
                                                password=cls._password,
                                                port=cls._dbPort,
                                                database=cls._dataBase)
                
                log.debug(f'Conexion exitosa {cls._conexion}')
                return cls._conexion
            except Exception as e:
                log.error(f'Ocurrio una excepcion al obtener la conexion {e}')
                sys.exit()
        else:
            return cls._conexion

    @classmethod
    def obtenerCursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                log.debug(f'Se abrio correctamente el cursor: {cls._cursor}')
                return cls._cursor
            except Exception as e:
                log.error(f'Ocurrio una excepcion al obtener el cursor: {e}')
                sys.exit()
        else:
            return cls._cursor

if __name__ == '__main__':
    conexion.obtenerConexion()