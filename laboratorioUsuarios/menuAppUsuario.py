from usuario import Usuario
from loggerBase import log
from usuarioDao import usuarioDao


opcion = None

while opcion != 5:
    print('Opciones:')
    print('1. Listar usuarios')
    print('2. Agregar usuario')
    print('3. Modificar usuario')
    print('4. Eliminar usuario')
    print('5. Salir')

    opcion = int(input('Escribe tu opcion (1-5): '))

    if opcion == 1:
        usuarios = usuarioDao.seleccionar()
        for usuario in usuarios:
            log.info(usuario)
    elif opcion == 2:
        usernameVar = input('Escribe el username: ')
        passwordVar = input('Escribe el password: ')
        usuario = Usuario(username=usernameVar, password=passwordVar)
        usuariosInsertados = usuarioDao.insertar(usuario)
        log.info(f'Usuarios insertados: {usuariosInsertados}')
    elif opcion == 3:
        idUsuarioNew = int(input('Escribe el id que quieres actualizar: '))
        newUsernameVar = input('Escribe el nuevo usuario: ')
        newPasswordVar = input('Escribe la nueva contraseña: ')
        usuario = Usuario(idUsuarioNew, newUsernameVar, newPasswordVar)
        usuarioActualizados = usuarioDao.actualizar(usuario)
        log.info(f'Usuario actualizado: {usuarioActualizados}')
    elif opcion == 4:
        deleteUser = int(input('Ingrese el numero del idUsuario a eliminar: '))
        usuario = Usuario(id_usuario=deleteUser)
        usuarioEliminados = usuarioDao.eliminar(usuario)
        log.info(f'Usuario eliminado: {usuarioEliminados}')
    else:
        log.info('Salimos de la aplicacion')