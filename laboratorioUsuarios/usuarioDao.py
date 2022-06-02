from cursorDelPool import cursorDelPool
from loggerBase import log
from usuario import Usuario


class usuarioDao:
    _SELECCIONAR = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO usuario (username, password) VALUES (%s, %s) '
    _ACTUALIZAR = 'UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario=%s'

    @classmethod
    def seleccionar(cls):
        with cursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registrosRecuperados = cursor.fetchall()
            usuarios = []
            for registro in registrosRecuperados:
                print(f'Registros recuperados: {registrosRecuperados} ')
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
                return usuarios

    @classmethod
    def insertar(cls, usuario):
        with cursorDelPool() as cursor:
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Personas insertadas: {usuario} ')
            return cursor.rowcount
    
    @classmethod
    def actualizar(cls, usuario):
        with cursorDelPool() as cursor:
            valores = (usuario.username, usuario.password, usuario.idUsuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Registros actualizados: {usuario} ')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, usuario):
        with cursorDelPool() as cursor:
            valores = (usuario.idUsuario,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Registro eliminado {usuario} ')
            return cursor.rowcount

if __name__ == '__main__':
    
    #Seleccionar
    usuarios = usuarioDao.seleccionar()
    for usuario in usuarios:
        log.debug(usuario)

    #Insertar
    #usuario1 = Usuario(username='Pedro', password='pedro123' )
    #usuariosInsertados =  usuarioDao.insertar(usuario1)
    #log.debug(f'Usuarios insertadas: {usuariosInsertados}')

    #Actualizar
    #usuario2 = Usuario(2, username='David', password='David123')
    #usuariosActualizados = usuarioDao.actualizar(usuario2)
    #log.debug(f'Usuario actualizado: {usuariosActualizados}')

    #Eliminar
    usuario3 = Usuario(id_usuario=2)
    usuarioEliminado = usuarioDao.eliminar(usuario3)
    log.debug(f'Usuario eliminado: {usuarioEliminado}')